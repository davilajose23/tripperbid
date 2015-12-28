from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from mysite import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile

import unicodedata

# Create your views here.
from .forms import SettingsForm_gen
from .models import Usuario, Subasta, Piramide, UsuarioPiramide, Follows, Ganador
from .utils import generic_search


def Index(request):

	return render(request,'trips/index.html')

def Login(request):

	next = request.GET.get('next', '/proyectos/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']


		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/trips/')
			else:
				return HttpResponse("Inactive user.")
		else:
			#	return HttpResponseRedirect(settings.LOGIN_URL)
			return HttpResponseRedirect('/login/')

	if request.user.is_authenticated():
		return HttpResponseRedirect('/trips/')

	return render(request,'trips/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/trips/')

def Registro(request):
	#falta checar que el email sea unico

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        date_birth = request.POST['birth']
        gender  = request.POST['gender']

        mailused = None
        try:
        	mailused = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
        	print("usuario no existe")

		if mailused is None:
			user = User.objects.create_user(username=email, email=email, password=password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			usuario = Usuario(
	            first_name=first_name,last_name=last_name,password=password,
	            email=email,user=user)
			usuario.save()

        #send_mail('Bienvenido a Incubadora Caracol', ':', 'noreply@incubadoracaracol.com',[usuario.email], fail_silently=False)
        	return render_to_response('trips/login.html', RequestContext(request))

	if request.user.is_authenticated():
		return HttpResponseRedirect('/trips/')

    return render_to_response('trips/signup.html',  RequestContext(request))


def Trips(request):

	subastas = Subasta.objects.all()

	return render(request,'trips/trips.html',{'subastas':subastas})

def Details(request,sub_id):

	subasta = Subasta.objects.get(pk=sub_id)
	piramide = Piramide.objects.filter(subasta__id=sub_id,finished=False)


	if piramide is None:
		piramide = Piramide(subasta=sub_id)

	usuariopiramide = UsuarioPiramide.objects.order_by('nivel').filter(piramide__subasta__pk=sub_id,finished=False)
	cantidad = usuariopiramide.count()
	recaudado = cantidad * subasta.precio
	vacios = 14 - cantidad

	if request.user.is_authenticated():
		for up in usuariopiramide:
			if up.usuario.id == request.user.usuario.id:

				return render(request,'trips/details.html',{'subasta':subasta,'piramide':piramide,
				'usuariopiramide':usuariopiramide,'piramide_usuario':up.piramide,'cantidad':cantidad,'recaudado':recaudado,'participa':True,'vacios':vacios})

	return render(request,'trips/details.html',{'subasta':subasta,'piramide':piramide,
		'usuariopiramide':usuariopiramide,'cantidad':cantidad,'recaudado':recaudado,'vacios':vacios})

def inscribir_subasta(request,sub_id, p_id ):

	pir_vacia = Piramide.objects.filter(subasta__id=sub_id)
	subasta = Subasta.objects.get(pk=sub_id)

	if not pir_vacia.exists():
		#hacer una nva pira
		piramide = Piramide(subasta=subasta)
		piramide.save()
	else:
		try:
			piramide = Piramide.objects.get(pk=p_id)
		except Piramide.DoesNotExist:
			raise Http404("No existe esta piramide")

	try:
		user = Usuario.objects.get(pk=request.user.usuario.pk)
	except Usuario.DoesNotExist:
		raise Http404("No existe ese usuario")

	pir = UsuarioPiramide.objects.filter(usuario__pk=user.id, piramide__pk=piramide.id)

    #se checa si ya estaba registrado el usuario en la piramide y lo agrega
	if not pir:
    	#registrar
		up = UsuarioPiramide(usuario=user,piramide=piramide)
		up.nivel = piramide.inscritos + 1
		up.save()
		piramide.inscritos += 1
		piramide.save()

	#checa si ya se lleno la piramide y la divide
	pir = UsuarioPiramide.objects.filter(piramide=piramide)

	if piramide.inscritos  >= piramide.limite:
		# se lleno hay que crear dos nvas piramides
		pir_izq = Piramide(subasta=subasta)
		pir_izq.save()

		pir_der = Piramide(subasta=subasta)
		pir_der.save()

		izq = [2,4,5,8,9,10,11]
		der = [3,6,7,12,13,14,15]
		contador = 0
		for userpir in pir :

			if userpir.nivel == 1:
				#mover a ganadores
				ganador = Ganador(usuario=userpir.usuario,subasta=subasta,cantidad=subasta.pago)
				ganador.save()

			if userpir.nivel in izq:
				up  = UsuarioPiramide(usuario=userpir.usuario,piramide=pir_izq)
				up.nivel = pir_izq.inscritos + 1
				up.save()
				pir_izq.inscritos += 1
				pir_izq.save()


			if userpir.nivel in der:
				up  = UsuarioPiramide(usuario=userpir.usuario,piramide=pir_der)
				up.nivel = pir_der.inscritos + 1
				up.save()
				pir_der.inscritos += 1
				pir_der.save()

			userpir.finished = True
			userpir.save()

		#eliminar la piramide pasada o hacerla finished
		piramide.finished = True
		piramide.save()

	return HttpResponseRedirect('/details/'+sub_id)


def Follow(request,user_id):
	next = request.GET.get('next', '/')

	if request.user.is_authenticated():
		try:
			followed = Usuario.objects.get(pk=user_id)
		except Usuario.DoesNotExist:
			raise Http404("No existe este usuario")
			#ssss
		try:
			follower = Usuario.objects.get(pk=request.user.usuario.pk)
		except Usuario.DoesNotExist:
			raise Http404("No existe ese usuario")

		relation = Follows.objects.filter(followed=followed,follower=follower)


		if not relation.exists() and  not request.user.usuario == followed:
			#crear la relacion Follow
			relacion2 = Follows(followed=followed,follower=follower)
			relacion2.save()
			return HttpResponseRedirect('/profile/'+user_id)

	return HttpResponseRedirect('/profile/'+user_id)


def Unfollow(request,user_id):
	next = request.GET.get('next', '/')

	if request.user.is_authenticated():
		try:
			followed = Usuario.objects.get(pk=user_id)
		except Usuario.DoesNotExist:
			raise Http404("No existe este usuario")
			#ssss
		try:
			follower = Usuario.objects.get(pk=request.user.usuario.pk)
		except Usuario.DoesNotExist:
			raise Http404("No existe ese usuario")

		relation = Follows.objects.filter(followed=followed,follower=follower)


		if relation.exists():
			#delete la relacion Follow
			relation.delete()

			return HttpResponseRedirect('/profile/'+user_id)

	return HttpResponseRedirect('/profile/'+user_id)

def Profile(request,prof_id):

	usuario= Usuario.objects.get(pk=prof_id)

	if request.user.is_authenticated():

		follower = Usuario.objects.get(pk=request.user.usuario.pk)

		relation = Follows.objects.filter(followed=usuario,follower=follower)

		if relation.exists():
			return render(request,'trips/profile.html',{'usuario':usuario,'follow':True})

	return render(request,'trips/profile.html',{'usuario':usuario})

def Profile_about(request,prof_id):
	usuario= Usuario.objects.get(pk=prof_id)
	if request.user.is_authenticated():

		follower = Usuario.objects.get(pk=request.user.usuario.pk)

		relation = Follows.objects.filter(followed=usuario,follower=follower)

		if relation.exists():
			return render(request,'trips/profile_about.html',{'usuario':usuario,'follow':True})
	return render(request,'trips/profile_about.html',{'usuario':usuario})

def Profile_followers(request,prof_id):
	usuario= Usuario.objects.get(pk=prof_id)
	relaciones = Follows.objects.filter(followed=usuario)

	if request.user.is_authenticated():

		follower = Usuario.objects.get(pk=request.user.usuario.pk)

		relation = Follows.objects.filter(followed=usuario,follower=follower)

		if relation.exists():

			return render(request,'trips/profile_followers.html',{'usuario':usuario,'relaciones':relaciones,'follow':True})
	return render(request,'trips/profile_followers.html',{'usuario':usuario,'relaciones':relaciones})

def Profile_following(request,prof_id):
	usuario= Usuario.objects.get(pk=prof_id)
	relaciones = Follows.objects.filter(follower=usuario)
	if request.user.is_authenticated():

		follower = Usuario.objects.get(pk=request.user.usuario.pk)
		relation = Follows.objects.filter(followed=usuario,follower=follower)

		if relation.exists():
			return render(request,'trips/profile_following.html',{'usuario':usuario,'relaciones':relaciones,'follow':True})

	return render(request,'trips/profile_following.html',{'usuario':usuario,'relaciones':relaciones})


QUERY="search-query"

MODEL_MAP = { Subasta  : ["nombre", "precio"],
				Usuario: ["first_name","last_name",],


   }

def Search(request):



	objects = []
	size = 0
	for model,fields in MODEL_MAP.iteritems():
		objects+=generic_search(request,model,fields,"search-query")
		size += 1
	return render(request,"trips/search.html",
                             {"objects":objects,
                              "search_string" : request.GET.get(QUERY,""),
                              "size" : len(objects)
                          }
   )

def Settings_gen(request):



	if request.user.is_authenticated():


		data={'first_name': request.user.usuario.first_name,
								'last_name': request.user.usuario.last_name,
								'email':request.user.usuario.email}
		form = SettingsForm_gen(data)

		if request.method == "POST":

			form = SettingsForm_gen(request.POST,request.FILES)

			if form.is_valid():

				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				email = form.cleaned_data['email']

				user = User.objects.get(username=request.user.username)
				usuario = user.usuario

				usuario.first_name = first_name
				usuario.last_name = last_name

				# TODO: checar que no se repita el email
				#usuario.email = email
				#user.username = email
				user.first_name = first_name
				user.last_name = last_name
				pp = form.cleaned_data['pp']

				if pp:
					usuario.pp=pp
				user.save()
				usuario.save()

				data={'first_name': request.user.usuario.first_name,
										'last_name': request.user.usuario.last_name,
										'email':request.user.usuario.email}
				form = SettingsForm_gen(data)
				return HttpResponseRedirect('/settings/')


			#first_name = request.POST.get('first_name',request.user.usuario.first_name)
			#last_name = request.POST.get('last_name',request.user.usuario.last_name)
			#email = request.POST.get('email',request.user.usuario.first_name)
			#gender = request.POST.get('gender',request.user.usuario.last_name)

			'''
							user = User.objects.get(username=request.user.username)
							usuario = user.usuario

							usuario.first_name = first_name
							usuario.last_name = last_name

							# TODO: checar que no se repita el email
							#usuario.email = email
							#user.username = email
							user.first_name = first_name
							user.last_name = last_name
							user.save()
							usuario.save()
			'''

		return render(request,'trips/settings.html',{'user':request.user,'form':form})
	else:
		return HttpResponseRedirect('/trips/')

def Settings_prof(request):

	if request.user.is_authenticated():

		return render(request,'trips/settings.html',{'user':request.user})
	else:
		return HttpResponseRedirect('/trips/')

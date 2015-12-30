import datetime

from django.db import models
from .utils import OverwriteStorage
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

fs = FileSystemStorage(location='media/photos')

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	lista = filename.split('.')
	extension = lista[len(lista)-1]
	filename = 'pp.'+extension

	ruta = 'user_{0}/{1}'.format(instance.user.id, filename)
	return ruta

class Usuario(models.Model):
	GENDER_CHOICE = (
        ('F', 'female'),
        ('M', 'male'),
        ('O', 'other'),
    )
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	password = models.CharField(max_length=50,null=True)
	email = models.EmailField(max_length=254,default='example@example.com',unique=True)
	date = models.DateTimeField('register date', default=datetime.datetime.now())
	pp = models.ImageField(upload_to = user_directory_path,storage=OverwriteStorage(), default = 'photos/foto.jpg')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default='O')
	def __str__(self):              # __unicode__ on Python 2
		return self.first_name+" "+self.last_name

class Follows(models.Model):
	follower = models.ForeignKey(Usuario,related_name="follower_user")
	followed = models.ForeignKey(Usuario,related_name="followed_user")

	def __str__(self):
		return self.follower.first_name+" follows "+self.followed.first_name

class Subasta(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	precio = models.IntegerField(default=10)
	pago = models.IntegerField(default=0)
	recaudado = models.IntegerField(default=0)
	def __str__(self):              # __unicode__ on Python 2
		return self.nombre

class Piramide(models.Model):
	subasta = models.ForeignKey(Subasta)
	finished = models.BooleanField(default=False)
	#limite 14
	inscritos = models.IntegerField(default=0)
	limite = models.IntegerField(default=15)

	def __str__(self):              # __unicode__ on Python 2
		return self.subasta.nombre

class UsuarioPiramide(models.Model):
	usuario = models.ForeignKey(Usuario)
	piramide = models.ForeignKey(Piramide)
	lider = models.BooleanField(default=False)
	nivel = models.IntegerField(default= 1)
	finished = models.BooleanField(default=False)
	#date
	date = models.DateTimeField('date payed', default=datetime.datetime.now())

	def __str__(self):              # __unicode__ on Python 2
		return self.usuario.first_name+" "+self.piramide.subasta.nombre

class Ganador(models.Model):
	usuario = models.ForeignKey(Usuario)
	subasta = models.ForeignKey(Subasta)
	cantidad = models.IntegerField(default=0)
	date = models.DateTimeField('date win', default=datetime.datetime.now())
	cobrado = models.BooleanField(default=False)

	def __str__(self):              # __unicode__ on Python 2
		return self.usuario.first_name+" gano en la subasta: "+self.subasta.nombre

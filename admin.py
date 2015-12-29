from django.contrib import admin

# Register your models here.

from .models import Usuario, Subasta, Piramide, UsuarioPiramide, Follows,Ganador

class UsuarioAdmin(admin.ModelAdmin):
    # ...
    list_display = ('first_name', 'last_name', 'email','date')
    list_filter = ['first_name','last_name','date']
    search_fields = ['first_name','last_name','email']

class GanadorAdmin(admin.ModelAdmin):
    # ...
    list_display = ('usuario','usuario_first_name','usuario_last_name','subasta','cantidad','date','cobrado')

    list_filter = ['usuario__first_name','usuario__last_name','date','subasta','cantidad','cobrado']

    search_fields = ['usuario__first_name','usuario__last_name','date','subasta','cantidad']


    def usuario_first_name(self,obj):
        return obj.usuario.first_name

    def usuario_last_name(self,obj):
        return obj.usuario.last_name

    usuario_first_name.admin_order_field = 'usuario__first_name'
    usuario_last_name.admin_order_field = 'usuario__last_name'

class UsuarioPiramideAdmin(admin.ModelAdmin):

    list_display = ('usuario','subasta','date','cantidad','finished','nivel')


    def subasta(self,obj):
        return obj.piramide.subasta

    def cantidad(self,obj):
        return obj.piramide.subasta.precio

    subasta.admin_order_field = 'piramide__subasta'
    subasta.admin_order_field = 'piramide__subasta_precio'

admin.site.register(Subasta)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Piramide)
admin.site.register(UsuarioPiramide,UsuarioPiramideAdmin)
admin.site.register(Follows)
admin.site.register(Ganador,GanadorAdmin)

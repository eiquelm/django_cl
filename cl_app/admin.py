from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','habilitada','margporc','valormag','slug',)
    resources_class = CategoriaResource

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre','codigo']
    list_display = ('nombre','codigo','direccion','Telefono','Provincia','correo',)

class EntidadAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion','telefono','cuentaCUP','titularCUP','cuentaCL', 'titularCL','bancoCUP','cuentaEst', 'vigencia','margen',)

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo

class ArticuloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['codigo','descrip',]
    list_display = ('codigo','descrip','um','precioCUP','precioCL','habilitado',)

admin.site.register(Entidad,EntidadAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)

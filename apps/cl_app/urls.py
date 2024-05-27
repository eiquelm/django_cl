from django.urls import path
from .views import ListarCat, EditarCat, CrearCat, EliminarCat


urlpatterns = [
    path('listar_categorias/',ListarCat.as_view(), name='listar_categorias'),
    path('crear_categoria/',CrearCat.as_view(), name='crear_categoria'),
    path('editar_categorias/<slug:slug>', EditarCat.as_view(), name='editar_categoria'),
    path('eliminar_categoria/<slug:slug>/', EliminarCat.as_view(), name='eliminar_categoria'),

]

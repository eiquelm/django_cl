from django.urls import path, include
from .views  import *
from . import views

urlpatterns = [
    path('',home, name='index'),
    path('categorias/', views.categoria, name="categorias"),
    path('categorias/eliminarCategoria/<slug:slug>', views.eliminarCategoria),

]

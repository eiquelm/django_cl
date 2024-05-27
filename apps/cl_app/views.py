from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Categoria
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import CategoriaForm
from django.urls import reverse_lazy

# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'

class ListarCat(ListView):
    model = Categoria
    template_name = 'Categorias/listarCat.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.all()

class EditarCat(UpdateView):
    model = Categoria 
    template_name = 'Categorias/crearCat.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('cl_app:listar_categorias')

class CrearCat(CreateView):
    model = Categoria
    template_name = 'Categorias/crearCat.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('cl_app:listar_categorias')

class EliminarCat(DeleteView):
    model = Categoria
    success_url = reverse_lazy('cl_app:listar_categorias')



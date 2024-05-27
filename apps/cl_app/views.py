from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Categoria
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import CategoriaForm
from django.urls import reverse_lazy

# Create your views here.

class Inicio(TemplateView):
    template_name = 'cl_app/index.html'

class ListarCat(ListView):
    model = Categoria
    template_name = 'Categorias/listarCat.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.all()

class EditarCat(UpdateView):
    model = Categoria 
    template_name = 'Categorias/editarCat.html'
    form_class = CategoriaForm
    #success_url = reverse_lazy('cl_app:listar_categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('cl_app:listar_categorias')    

class CrearCat(CreateView):
    model = Categoria
    template_name = 'Categorias/crearCat.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('cl_app:listar_categorias')

class EliminarCat(DeleteView):
    model = Categoria
    success_url = reverse_lazy('cl_app:listar_categorias')



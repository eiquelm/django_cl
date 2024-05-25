from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Categoria
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'index.html')

def categoria(request):
    title = 'Listado de Categorias'
    categorias = Categoria.objects.all()
    #categorias = Categoria.objects.filter(habilitada = True) habilitada__iexact
    return render(request, 'Categorias/listarCat.html', {
        'categorias': categorias
    })

def eliminarCategoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    #categoria = Categoria.objects.get(slug=slug)
    categoria.delete()
    return HttpResponseRedirect('/categorias')

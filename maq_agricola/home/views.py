from django.shortcuts import render, get_object_or_404
from .models import Anuncio

def index(request):
    query = request.GET.get('q')  # Obtém o termo de busca do GET
    anuncios = Anuncio.objects.all()

    if query:
        anuncios = anuncios.filter(
            marca__icontains=query
        ) | anuncios.filter(
            descricao__icontains=query
        )  # Filtra por marca ou descrição (insensível a maiúsculas/minúsculas)

    return render(request, 'home/index.html', {'anuncios': anuncios})  # Caminho corrigido

def detalhe_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    return render(request, 'home/detalhe_anuncio.html', {'anuncio': anuncio})  # Caminho correto

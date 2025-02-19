from django.shortcuts import render, get_object_or_404
from .models import Anuncio

def index(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'home/index.html', {'anuncios': anuncios})  # Caminho corrigido

def detalhe_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    return render(request, 'home/detalhe_anuncio.html', {'anuncio': anuncio})  # Caminho corrigido



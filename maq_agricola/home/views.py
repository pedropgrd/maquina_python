from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Importando mensagens
from django.contrib.auth.decorators import login_required
from .models import Anuncio, Anunciante
from .forms import AnuncioForm
from .forms import RegistroAnuncianteForm

# Página inicial
def index(request):
    query = request.GET.get('q')
    anuncios = Anuncio.objects.all()
    if query:
        anuncios = anuncios.filter(marca__icontains=query) | anuncios.filter(descricao__icontains=query)
    return render(request, 'home/index.html', {'anuncios': anuncios})

# Detalhes do anúncio
def detalhe_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    return render(request, 'home/detalhe_anuncio.html', {'anuncio': anuncio})

# Registrar anunciante
def registrar_anunciante(request):
    if request.method == 'POST':
        form = RegistroAnuncianteForm(request.POST)
        if form.is_valid():
            form.save()  # Não loga automaticamente, apenas cria o usuário
            messages.success(request, "Cadastro realizado com sucesso! Agora, faça login.")  # Mensagem de sucesso
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os dados informados.")  # Mensagem de erro
    else:
        form = RegistroAnuncianteForm()
    return render(request, 'auth/registro.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('gerenciar_anuncios')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('index')

# Gerenciar anúncios (apenas para anunciantes logados)
@login_required  # Garantindo que só usuários logados possam acessar
def gerenciar_anuncios(request):
    anuncios = Anuncio.objects.filter(anunciante__user=request.user)
    return render(request, 'anuncios/gerenciar.html', {'anuncios': anuncios})

def gerenciamento(request):
    anuncios = Anuncio.objects.all()
    form = AnuncioForm()
    return render(request, 'anuncios/cadastro_anuncios.html', {'anuncios': anuncios, 'form': form})

def criar_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gerenciamento')
    return redirect('gerenciamento')

def editar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('gerenciamento')
    return redirect('gerenciamento')

def deletar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    anuncio.delete()
    return redirect('gerenciamento')

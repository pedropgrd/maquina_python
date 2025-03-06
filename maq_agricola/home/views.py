from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Importando mensagens
from django.contrib.auth.decorators import login_required
from .models import Anuncio, Anunciante
from .forms import AnuncioForm
from .forms import RegistroAnuncianteForm
from .forms import PerfilAnuncianteForm 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import PerfilAnuncianteForm

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
            messages.success(request, "Login realizado com sucesso!")
            return redirect('gerenciar_anuncios')
        else:
            messages.error(request, "Usuário ou senha incorretos. Tente novamente.")

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

@login_required
def editar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)

    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            messages.success(request, "Anúncio atualizado com sucesso!")
            return redirect('gerenciamento')
        else:
            messages.error(request, "Erro ao editar anúncio. Verifique os dados informados.")
    else:
        form = AnuncioForm(instance=anuncio)

    return render(request, 'anuncios/editar_anuncio.html', {'form': form, 'anuncio': anuncio})



@login_required
def deletar_anuncio(request, id):
    # Obtém o anúncio a ser deletado
    anuncio = get_object_or_404(Anuncio, id=id)
    anuncio.delete()  # Exclui o anúncio
    return redirect('gerenciamento')  # Redireciona para a lista de anúncios


@login_required
def perfil_anunciante(request):
    user = request.user
    if request.method == "POST":
        form = PerfilAnuncianteForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)  # Salva os outros campos
            nova_senha = form.cleaned_data.get("nova_senha")
            
            if nova_senha:
                user.set_password(nova_senha)  # Atualiza a senha corretamente
                update_session_auth_hash(request, user)  # Mantém o usuário logado após alterar a senha
            
            user.save()
            return redirect('perfil_anunciante')
    else:
        form = PerfilAnuncianteForm(instance=user)

    return render(request, 'auth/perfil_anunciante.html', {'form': form})

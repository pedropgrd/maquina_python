from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Anunciante
from .models import Anuncio  # Certifique-se de que essa linha está presente
from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class RegistroAnuncianteForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")
    telefone = forms.CharField(max_length=15, required=True, label="Telefone")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'telefone']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            Anunciante.objects.create(user=user, telefone=self.cleaned_data['telefone'])
        return user



class PerfilAnuncianteForm(UserChangeForm):
    nova_senha = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label="Nova senha"
    )
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label="Confirmar senha"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'nova_senha', 'confirmar_senha']

    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get("nova_senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if nova_senha and nova_senha != confirmar_senha:
            self.add_error("confirmar_senha", "As senhas não coincidem.")

        return cleaned_data

        
class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'descricao', 'categoria', 'marca', 'modelo', 'ano', 'preco', 'imagem']
    
    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Anunciante
from .models import Anuncio  # Certifique-se de que essa linha está presente

class RegistroAnuncianteForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, required=True, label="Telefone")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'telefone']

    def save(self, commit=True):
        # Criação do usuário
        user = super().save(commit=False)
        if commit:
            user.save()
            # Criar o objeto Anunciante associado ao usuário
            Anunciante.objects.create(user=user, telefone=self.cleaned_data['telefone'])
        return user

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'descricao', 'categoria', 'marca', 'modelo', 'ano', 'preco', 'imagem']
        # 
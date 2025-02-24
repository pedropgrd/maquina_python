from django.contrib.auth.models import User
from django.db import models

class Anunciante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Anuncio(models.Model):
    CATEGORIAS = (
        ('Trator', 'Trator'),
        ('Colheitadeira', 'Colheitadeira'),
        ('Caminhão', 'Caminhão'),
        ('Outros', 'Outros'),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    telefone_contato = models.CharField(max_length=15, blank=True, null=True)
    imagem = models.ImageField(upload_to='imagens_anuncios/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    anunciante = models.ForeignKey(Anunciante, on_delete=models.SET_NULL, null=True)

    def get_imagem_url(self):
        if self.imagem:
            return self.imagem.url
        return '/static/img/default.jpg'

    def __str__(self):
        return self.titulo

from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


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
    imagem = models.ImageField(upload_to='imagens_anuncios/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def get_imagem_url(self):
        if self.imagem:
            return self.imagem.url
        return '/static/img/default.jpg'  # Caminho da imagem padrão

    def __str__(self):
        return self.titulo



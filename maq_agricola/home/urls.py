from django.urls import path
from . import views

urlpatterns = [
    path('', views.seja_bem_vindo, name='seja_bem_vindo'),  # Rota para a página inicial
]


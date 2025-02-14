# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.seja_bem_vindo, name='seja_bem_vindo'),  # Rota para a página inicial
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anuncio/<int:anuncio_id>/', views.detalhe_anuncio, name='detalhe_anuncio'),
]

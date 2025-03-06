from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Importa todas as views corretamente

urlpatterns = [
    path('registrar/', views.registrar_anunciante, name='registrar_anunciante'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('gerenciar/', views.gerenciar_anuncios, name='gerenciar_anuncios'),
    path('gerenciamento/', views.gerenciamento, name='gerenciamento'),
    path('criar/', views.criar_anuncio, name='criar_anuncio'),
    path('editar/<int:id>/', views.editar_anuncio, name='editar_anuncio'),
    path('perfil/', views.perfil_anunciante, name='perfil_anunciante'),
    path('deletar/<int:id>/', views.deletar_anuncio, name='deletar_anuncio'),
    path('', views.index, name='index'),
    path('anuncio/<int:anuncio_id>/', views.detalhe_anuncio, name='detalhe_anuncio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

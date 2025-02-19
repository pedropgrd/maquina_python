
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anuncio/<int:anuncio_id>/', views.detalhe_anuncio, name='detalhe_anuncio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



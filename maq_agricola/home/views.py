from django.shortcuts import render


def seja_bem_vindo(request):
    return render(request, 'index.html')  # Renderiza o template


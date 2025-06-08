from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def servicos(request):
    return render(request, 'core/servicos.html')

def avaliacoes(request):
    return render(request, 'core/avaliacoes.html')

def sobre(request):
    return render(request, 'core/sobre.html')

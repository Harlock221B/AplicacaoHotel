from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def sobre(request):
    return render(request, 'sobre_nos.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def hoteis(request):
    return render(request, 'hoteis.html')

def reserva(request):
    return render(request, 'reserva.html')    

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='homepage'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('hoteis/', views.hoteis, name='hoteis'),
    path('reserva/', views.reserva, name='reserva'),
    path('sobre/', views.sobre, name='sobre'),
]
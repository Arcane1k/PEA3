from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('sobre/', views.sobre, name='sobre'),
]

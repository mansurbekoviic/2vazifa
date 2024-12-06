from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kurtua/', views.kurtua, name='kurtua'),
    path('carvajal/', views.carvajal, name='carvajal'),
    path('militao/', views.militao, name='militao'),
    path('ramos/', views.ramos, name='ramos'),
    path('bellingham/', views.bellingham, name='bellingham'),
    path('camavinga/', views.camavinga, name='camavinga'),
    path('vinicius/', views.vinicius, name='vinicius'),
    path('valverde', views.valverde, name='valverde'),
    path('mbappe/', views.mbappe, name='mbappe'),
    path('modric/', views.modric, name='modric'),
]

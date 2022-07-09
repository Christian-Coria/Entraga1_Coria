from django.contrib import admin
from django.urls import path
from mi_web.views import registrando_cliente, registrando_equipos, reparando

urlpatterns = [
   path('clientes/', registrando_cliente),
   path('equipos/', registrando_equipos),
   path('reparaciones/', reparando),
   
]
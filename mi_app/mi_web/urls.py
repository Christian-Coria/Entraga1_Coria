from django.contrib import admin
from django.urls import path
from mi_web.views import (registrando_proveedores,
 registrando_repuestos, registrando_reparaciones,formulario_reparacion,formulario_proveedores,
 formulario_repuestos,form_busc_proveedor,form_busc_reparacion,form_busc_repuesto)

urlpatterns = [
   path('lista_reparaciones/', registrando_reparaciones),
   path('lista_repuestos/', registrando_repuestos),
   #path('reparaciones/', reparando),
   path('lista_proveedores/',registrando_proveedores),
   path('proveedores/',formulario_proveedores),
   path('repuestos/',formulario_repuestos),
   path('busqueda_proveedor/',form_busc_proveedor),
   path('busqueda_reparacion/',form_busc_reparacion),
   path('busqueda_repuestos/',form_busc_repuesto),
   
]
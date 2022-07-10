from django.contrib import admin
from django.urls import path
from mi_web.views import (registrando_cliente,
 registrando_equipos, reparando,formulario_reparacion,formulario_proveedores,
 formulario_repuestos,form_busc_proveedor,form_busc_reparacion,form_busc_repuesto)

urlpatterns = [
   path('clientes/', registrando_cliente),
   path('equipos/', registrando_equipos),
   path('reparaciones/', reparando),
   path('ordenes/',formulario_reparacion),
   path('proveedores/',formulario_proveedores),
   path('repuestos/',formulario_repuestos),
   path('busqueda_proveedor/',form_busc_proveedor),
   path('busqueda_reparacion/',form_busc_reparacion),
   path('busqueda_repuestos/',form_busc_repuesto),
   
]
from django.contrib import admin
from django.urls import path
from mi_web.views import (registrando_proveedores,
 registrando_repuestos, registrando_reparaciones,formulario_reparacion,formulario_proveedores,
 formulario_repuestos,form_busc_proveedor,form_busc_reparacion,form_busc_repuesto)

urlpatterns = [
   path('listando_repa/', registrando_reparaciones),
   path('listando_repu/', registrando_repuestos),
   path('listando_prov/',registrando_proveedores),
   path('reparaciones/',formulario_reparacion),
   path('proveedores/',formulario_proveedores),
   path('repuestos/',formulario_repuestos),
   path('busqueda_proveedor/',form_busc_proveedor),
   path('busqueda_reparacion/',form_busc_reparacion),
   path('busqueda_repuestos/',form_busc_repuesto),
   
]
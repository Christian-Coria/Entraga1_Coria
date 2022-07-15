from django.contrib import admin
from django.urls import path
from mi_web.views import (registrando_proveedores,
 registrando_repuestos, registrando_reparaciones,formulario_reparacion,formulario_proveedores,
 formulario_repuestos,busc_prov,busc_repa,
 busc_repu,detalle_reparacion, detalle_cliente,registrando_clientes,actualizar_reparacion,confirmar_borrar_reparacion,borrar_reparacion,leer_reparacion)

urlpatterns = [
   path('listando-repa/', registrando_reparaciones),
   path('listando-repu/', registrando_repuestos),
   path('listando-clientes/', registrando_clientes),
   path('listando_prov/',registrando_proveedores),
   path('reparaciones/',formulario_reparacion),
   path('proveedores/',formulario_proveedores),
   path('repuestos/',formulario_repuestos),
   path('busqueda-proveedor/',busc_prov),
   path('busqueda-reparacion/',busc_repa),
   path('busqueda-repuestos/',busc_repu),
   path('detalle/<int:id>/reparacion/',detalle_reparacion,name="detalle-reparacion"),
   path('detalle/<int:id>cliente',detalle_cliente, name="detalle-cliente"),
   path('reparacion/<pk>/actualizar',actualizar_reparacion),
   path('reparacion/<pk>/confirmar-borrar',confirmar_borrar_reparacion,name="reparacion-confirmar-borrar"),
   path('reparacion/<pk>/borrar',borrar_reparacion,name="reparacion-borrar"),
   path('leer-reparacion',leer_reparacion),
]
from django.shortcuts import render
from mi_web.models import Reparacion, Repuestos,Proveedores
from mi_web.forms import (Formulario_reparacion, Formulario_proveedores,
 Formulario_repuestos,Busqueda_repuesto,Busqueda_proveedor,Busqueda_reparacion)

def registrando_repuestos(request):
    context = {}
    context['lista_repuestos'] = Repuestos.objects.all()

    return render(request,'mi_web/repuestos.html',context)

def registrando_proveedores(request):
    context = {}
    context['lista_proveedores'] = Proveedores.objects.all()

    return render(request,'mi_web/proveedores.html',context)
    
def registrando_reparaciones(request):
    context = {}
    context['lista_reparaciones'] = Reparacion.objects.all()

    return render(request,'mi_web/reparaciones.html',context)


def formulario_reparacion(request):
    if request.method == "POST":
        pass
    else:
        form_reparacion = Formulario_reparacion()
        return render (request, "mi_web/ordenes.html",{"form_reparacion":form_reparacion})

def formulario_proveedores(request):
    if request.method == "POST":
        pass
    else:
        form_proveedor = Formulario_proveedores()
        return render (request, "mi_web/proveedores.html",{"form_proveedor":form_proveedor})

def formulario_repuestos(request):
    if request.method == "POST":
        pass
    else:
        form_repuesto = Formulario_repuestos()
        return render (request, "mi_web/repuestos.html",{"form_repuesto":form_repuesto})

def form_busc_repuesto(request):
    busqueda_repuesto = Busqueda_repuesto()

    if request.GET:
        repuesto = Repuestos.objects.filter(nombre=busqueda_repuesto["criterio"]).all()
    
    else:
        repuesto=[]
    
    return render(request,'mi_web/busqueda_repuestos.html',{"busqueda_repuesto": Busqueda_repuesto,"repuesto":repuesto} )

def form_busc_proveedor(request):
    busqueda_proveedor = Busqueda_proveedor()

    if request.GET:
        proveedor = Proveedores.objects.filter(nombre=busqueda_proveedor["criterio"]).all()
       
    else:
        proveedor =[]
    return render(request,'mi_web/busqueda_proveedor.html',{"busqueda_proveedor": Busqueda_proveedor,"proveedor":proveedor})

def form_busc_reparacion(request):
    busqueda_reparacion = Busqueda_reparacion()

    if request.GET:
        reparacion = Reparacion.objects.filter(nombre=busqueda_reparacion["criterio"]).all()
    else:
        reparacion =[]
    return render(request,'mi_web/busqueda_reparacion.html',{"busqueda_reparacion": Busqueda_reparacion, "reparacion":reparacion})

 

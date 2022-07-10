from django.shortcuts import render
from mi_web.models import Reparacion, Repuestos,Proveedores
from mi_web.forms import (Formulario_reparacion, Formulario_proveedores,
 Formulario_repuestos,Busqueda_repuesto,Busqueda_proveedor,Busqueda_reparacion)

def registrando_cliente(request):
    context = {}
    context['lista_clientes'] = Cliente.objects.all()

    return render(request,'mi_web/clientes.html',context)

def registrando_equipos(request):
    context = {}
    context['lista_equipos'] = Equipo.objects.all()

    return render(request,'mi_web/equipos.html',context)
    
def reparando(request):
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
    if request.GET:
        busqueda_repuesto = Busqueda_repuesto(request.GET)
        criterio = Busqueda_repuesto.cleaned_data
        repuesto = Repuestos.objects.filter(nombre=criterio).all()
        return render(request,'mi_app/busqueda_repuestos.html',{"repuesto":repuesto})
    busqueda_repuesto = Busqueda_repuesto()
    return render(request,'mi_web/busqueda_repuestos.html',{"busqueda_repuesto": Busqueda_repuesto})

def form_busc_proveedor(request):
    if request.GET:
        busqueda_proveedor = Busqueda_proveedor(request.GET)
        criterio = Busqueda_proveedor.cleaned_data
        proveedor = Proveedores.objects.filter(nombre=criterio).all()
        return render(request,'mi_app/busqueda_proveedor.html',{"proveedor":proveedor})
    busqueda_proveedor = Busqueda_proveedor()
    return render(request,'mi_web/busqueda_proveedor.html',{"busqueda_proveedor": Busqueda_proveedor})

def form_busc_reparacion(request):
    if request.GET:
        busqueda_reparacion = Busqueda_reparacion(request.GET)
        criterio = Busqueda_reparacion.cleaned_data
        reparacion = Reparacion.objects.filter(nombre=criterio).all()
        return render(request,'mi_app/busqueda_reparacion.html',{"reparacion":reparacion})
    busqueda_reparacion = Busqueda_reparacion()
    return render(request,'mi_web/busqueda_reparacion.html',{"busqueda_reparacion": Busqueda_reparacion})



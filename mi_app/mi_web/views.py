from django.shortcuts import render
from mi_web.models import Cliente, Equipo, Reparacion
from mi_web.forms import Formulario_reparacion, Formulario_proveedores, Formulario_repuestos

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
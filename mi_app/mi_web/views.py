from django.shortcuts import render
from django.http  import HttpResponse
from mi_web.models import Reparacion, Repuestos,Proveedores,Cliente
from mi_web.forms import (Formulario_reparacion, Formulario_proveedores,
 Formulario_repuestos,Busqueda_repuesto,Busqueda_proveedor,Busqueda_reparacion)

def registrando_repuestos(request):
    nro_repuestos = Repuestos.objects.count()   #contabilizamos la cantidad de repuestos registrados
    lista_repuestos = Repuestos.objects.all()
    return render(request,'mi_web/listando_repu.html',{"nro_repuestos":nro_repuestos, "lista_repuestos": lista_repuestos}) 


def registrando_proveedores(request):
    nro_proveedores = Proveedores.objects.count()    #contabilizamos la cantidad de repuestos registrados
    lista_proveedores = Proveedores.objects.all()
    return render(request,'mi_web/listando_prov.html',{"nro_proveedores":nro_proveedores,"lista_proveedores":lista_proveedores})


def registrando_reparaciones(request):
    nro_reparaciones = Reparacion.objects.count()   #contabilizamos la cantidad de reparaciones registrados
    lista_reparaciones = Reparacion.objects.all()
    return render(request,'mi_web/listando_repa.html',{"lista_reparaciones":lista_reparaciones,"nro_reparaciones":nro_reparaciones})

def registrando_clientes(request):
    nro_cliente = Cliente.objects.count()   #contabilizamos la cantidad de reparaciones registrados
    lista_clientes = Cliente.objects.all()
    return render(request,'mi_web/listando_clientes.html',{"lista_clientes":lista_clientes,"nro_cliente":nro_cliente})


def detalle_reparacion(request, id):
    reparacion = get_objets_or_404(Reparacion,pk=pk) # get recuperamos el objeto
    return render(request, 'mi_web/detalle_reparacion.html',{'reparacion':reparacion})

def detalle_cliente(request, id):
    cliente = get_objets_or_404(Cliente,pk=pk) # get recuperamos el objeto
    return render(request, 'mi_web/detalle_reparacion.html',{'cliente':cliente})

def leer_reparacion(request):
    reparacion = Reparacion.objects.all()
    context = {"reparaciones":reparaciones}
    return

def formulario_reparacion(request):
    if request.method=="POST":
        form_reparacion = Formulario_reparacion(request.POST)
        if form_reparacion.is_valid():
            informacion = form_reparacion.cleaned_data

            reparacion= Reparacion(equipo=informacion['equipo'],falla=informacion['falla'],tipo_rep=informacion['tipo_rep'],estado=informacion['estado'])
            reparacion.save()
            return render (request, "mi_web/reparaciones.html")
    else:
         form_reparacion = Formulario_reparacion()
         return render (request, "mi_web/reparaciones.html",{"form_reparacion":form_reparacion})


def formulario_proveedores(request):
    if request.method=="POST":
        form_proveedor = Formulario_proveedores(request.POST)
        if form_proveedor.is_valid():
            informacion = form_proveedor.cleaned_data

            proveedor= Proveedores(nombre=informacion['nombre'],telefono=informacion['telefono'])
            proveedor.save()
            return render (request, "mi_web/proveedores.html")

    else:
        form_proveedor = Formulario_proveedores()
        return render (request, "mi_web/proveedores.html",{"form_proveedor":form_proveedor})




def formulario_repuestos(request):
    if request.method=="POST":
        form_repuesto = Formulario_repuestos(request.POST)
        if form_repuesto.is_valid():
            informacion = form_repuesto.cleaned_data

            repuesto= Repuestos(clase=informacion['clase'],marca=informacion['marca'],modelo=informacion['modelo'],precio=informacion['precio'])
            repuesto.save()
            return render (request, "mi_web/repuestos.html")
    else:
         form_repuesto = Formulario_repuestos()
         return render (request, "mi_web/repuesto.html",{"form_repuesto":form_repuesto})


def form_busc_repuesto(request):
    if request.GET:
        busqueda_repuestos = Formulario_repuestos(request.GET)
        if busqueda_repuestos.is_valid():
            repuestos = Repuestos.objects.filter(nombre=busqueda_repuestos.cleaned_data.get("criterio")).all() 
            return render(request, "mi_app/busqueda_repuestos.html", {"busqueda_repuestos": busqueda_repuestos, "repuestos": repuestos})

    return render(request, "mi_app/busqueda_repuestos.html", {"busqueda_repuestos": busqueda_repuestos, "repuestos": repuestos})

def form_busc_proveedor(request):
    if request.GET:
        busqueda_proveedores = Busqueda_proveedor(request.GET)
        criterio = Busqueda_proveedor.cleaned_data
        
        proveedor = Proveedores.objects.filter(nombre=criterio).all()
        return render(request, "mi_web/busqueda_proveedor.html", {"proveedor": proveedor})

    busqueda_proveedores =Busqueda_proveedor()
    return render(request, "mi_web/busqueda_proveedor.html",{"busqueda_proveedores":busqueda_proveedores})

    


def form_busc_reparacion(request):
    if request.GET:
        busqueda_reparaciones = formulario_reparacion(request)(request.GET)
        if busqueda_reparaciones.is_valid():
            reparacion = Reparacion().objects.filter(nombre=busqueda_reparaciones.cleaned_data.get("criterio")).all() 
            return render(request, "mi_app/busqueda_reparacion.html", {"busqueda_reparacion": busqueda_reparaciones, "reparacion": reparacion})

    return render(request, "mi_app/busqueda_reparacion.html", {"busqueda_reparacion": busqueda_reparaciones, "reparacion": reparacion})

 
def actualizar_reparacion(request,pk):
    if request.method == 'GET':
        reparacion = get_objets_or_404(Reparacion,pk=pk)
        initial = {"equipo":equipo,"falla":falla,"tipo_rep":tipo_rep,"estado":estado}
        formulario = Formulario_reparacion(initial=initial)
        return render(request,"mi_web/actualizar_reparacion.html", {"formulario":formulario})
    
    elif request.POST:
        formulario = Formulario_reparacion(request.POST)
        if formulario.is_valid():
            reparacion = get_objets_or_404(Reparacion,pk=pk)
            reparacion.equipo=formulario.cleaned_data.get("equipo")
            reparacion.falla=formulario.cleaned_data.get("falla")
            reparacion.tipo_rep=formulario.cleaned_data.get("tipo_rep")
            reparacion.estado=formulario.cleaned_data.get("estado")
            reparacion.save()
            return render(request,"mi_web/exito.html")

def confirmar_borrar_reparacion(request,pk):
    reparacion = get_objets_or_404(Reparacion,pk=pk)
    return render(request, "mi_web/confirmar_borrar.html",{"reparacion":reparacion})

def borrar_reparacion(request,pk):
    reparacion = get_objets_or_404(Reparacion,pk=pk)
    reparacion.delete()
    return render(request,"mi_web/exito.html")


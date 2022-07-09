from django.shortcuts import render
from mi_web.models import Cliente, Equipo, Reparacion

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



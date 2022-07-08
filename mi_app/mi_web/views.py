from django.shortcuts import render
from mi_web.models import Cliente, Equipo, Reparacion

def registrando_cliente(request):
    context = {}
    context[lista_clientes] = Cliente.objets.all()

    return render(request, 'mi_web/clientes.html',context)

def registrando_equipos(request):
    context = {}
    context[lista_equipos] = Equipo.objets.all()

    return render(request, 'mi_web/equipos.html',context)
def reparando(request):
    context = {}
    context[lista_reparaciones] = Reparacion.objets.all()

    return render(request, 'mi_web/reparaciones.html',context)



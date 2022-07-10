from django import forms
    
class Formulario_reparacion(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    telefono=forms.IntegerField()
    email=forms.EmailField()
    equipo = forms.CharField(max_length=40)
    falla = forms.CharField(max_length=40)

class Formulario_repuestos(forms.Form):
    clase = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    precio = forms.IntegerField()  
    
class Formulario_proveedores(forms.Form):
    nombre = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)



class Busqueda_reparacion(forms.Form):
    criterio = forms.CharField()

class Busqueda_proveedor(forms.Form):
    criterio = forms.CharField()

class Busqueda_repuesto(forms.Form):
    criterio = forms.CharField()
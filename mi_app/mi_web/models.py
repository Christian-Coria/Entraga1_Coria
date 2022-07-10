from django.db import models

class Reparacion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono=models.IntegerField()
    email=models.EmailField()
    equipo = models.CharField(max_length=40)
    falla = models.CharField(max_length=40)
    tipo_rep = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre {self.nombre}: {self.apellido} {self.telefono} {self.email} {self.equipo} {self.falla} {self.tipo_rep}  {self.estado}'

class Repuestos(models.Model):
    clase = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'Clase {self.clase}: {self.marca} {self.modelo} {self.falla} {self.precio}'

class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)

    def __str__(self):
        return f'Proveedor {self.nombre}: {self.telefono}'




from django.db import models
# creamos la Clase Equipo que no tiene relacion con otra clase
class Equipo(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    falla = models.CharField(max_length=40)

    def __str__(self):
        return f'Marca: {self.marca}: {self.modelo} {self.falla} '

# creamos la Clase Reparacion que no tiene relacion con otra clase
class Reparacion(models.Model):
    #marca = models.CharField(max_length=40)
    #modelo = models.CharField(max_length=40)
    #falla = models.CharField(max_length=40)
    tipo_rep = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)

    #definimos el metodo str para devolver en mejor formato la informacion
    def __str__(self):
        return f'Reparacion de {self.tipo_rep}: {self.estado}'

# creamos la Clase Cliente que tiene relacion con la clase Equipo y la clase Reparacion
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono=models.IntegerField()
    email=models.EmailField()
    #definimos las llaves foraneas de las tablas correspondiente a la clase Reparacion y Equipos
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    reparacion = models.ForeignKey(Reparacion, on_delete=models.SET_NULL, null=True) #con on_delete definimos el comportamiento 
                                                                                 # en caso de eliminar el registro, dejando por defecto el valor de NULL
    #definimos el metodo str para devolver en mejor formato la informacion
    def __str__(self):
        return f' Cliente {self.nombre}{self.apellido}: {self.telefono}, {self.email}, {self.reparacion}'







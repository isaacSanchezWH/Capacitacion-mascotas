from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_pa = models.CharField(max_length=40)
    apellido_ma = models.CharField(max_length=40)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellido_pa, self.apellido_ma)



class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

from django.db import models

# Create your models here.
class Empresa(models.Model):
	nombreEmp = models.CharField(max_length=30)
	direccion = models.CharField(max_length = 100)
	def __str__(self):
		return self.nombreEmp

class Departamento(models.Model):
	nombreD = models.CharField(max_length=30)
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombreD

class Empleado(models.Model):
	nombreE = models.CharField(max_length = 80)
	fechaNacimiento = models.DateField()
	email = models.EmailField()
	genero =  models.CharField(max_length = 1)
	telefono = models.IntegerField()
	celular = models.IntegerField()
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	fechaIngreso = models.DateField()
	def __str__(self):
		return self.nombreE



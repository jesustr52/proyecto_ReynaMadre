from django import forms
from .models import *

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ['nombreE', 'fechaNacimiento', 'email', 'genero', 'telefono', 'celular', 'empresa', 'departamento', 'fechaIngreso']

		
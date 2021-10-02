from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from .models import *
from .forms import EmpleadoForm


def login(request):
	return render(request, 'sistemaRM/login.html')

def home(request):
	empleados = Empleado.objects.all()
	context = {'empleados': empleados}
	return render (request, 'sistemaRM/home.html', context)

def agregar(request):
	if request.method == "POST":
		form = EmpleadoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = EmpleadoForm()
	context = {'form' : form}
	return render(request, 'sistemaRM/agregar.html', context)


def  eliminar(request, empleado_id):
	empleado = Empleado.objects.get(id =  empleado_id)
	empleado.delete()
	return redirect("home")

def editar(request, empleado_id):
	empleado = Empleado.objects.get(id=empleado_id)
	if request.method == "POST":
		form = EmpleadoForm(request.POST, instance=empleado)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = EmpleadoForm(instance=empleado)

	context = {"form" : form}
	return render(request, "sistemaRM/editar.html", context)

def logout_request(request):
	logout(request)

	return redirect("login")

def login_request(request):
	form = AuthenticationForm(request, data = request.POST)
	if form.is_valid():
		usuario = form.cleaned_data.get('username')
		contraseña = form.cleaned_data.get('password')
		user = authenticate(username = usuario, password=contraseña)

		if user is not None:
			login(request)
			return redirect("home")
		else:
			form = AuthenticationForm()
	else:
		form = AuthenticationForm()
	form = AuthenticationForm()
	return render(request,"sistemaRM/login.html", {"form" : form})
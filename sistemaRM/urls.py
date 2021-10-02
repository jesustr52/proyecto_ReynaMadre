from django.urls import path
from . import views

urlpatterns=[
	path("home/", views.home, name = 'home'),
	path("agregar/", views.agregar, name="agregar"),
	path("eliminar/<int:empleado_id>/", views.eliminar, name="eliminar"),
	path("editar/<int:empleado_id>/", views.editar, name="editar"),
	path("logout/", views.logout_request, name="logout"),
	path("", views.login_request, name="login"),
]
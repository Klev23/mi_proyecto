from django.urls import path
from mi_aplicacion.views import Escuelas, Home, EscuelaAlta , EscuelaEditar, EscuelaEliminar, Maestros, MaestroAlta, MaestroEditar, MaestroEliminar

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('escuelas', Escuelas.as_view(), name='escuelas'),
    path('alta', EscuelaAlta.as_view(), name='alta'),
    path('editar/<int:id>', EscuelaEditar.as_view(), name='editar'),
    path('eliminar/<int:id>', EscuelaEliminar.as_view(), name='eliminar'),
    path('maestros', Maestros.as_view(), name='maestros'),
    path('maestros/alta', MaestroAlta.as_view(), name='maestro_alta'),
    path('maestros/editar/<int:id>', MaestroEditar.as_view(), name='maestro_editar'),
    path('maestros/eliminar/<int:id>', MaestroEliminar.as_view(), name='maestro_eliminar'),
]

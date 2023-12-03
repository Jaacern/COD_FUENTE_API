from django.urls import path
from .views import registro_usuario, iniciar_sesion, user_create, reserva_create,lista_reservas, eliminar_reserva, inicio, perfil

urlpatterns = [
    path('registro/', registro_usuario, name='registro_usuario'),
    path('login/', iniciar_sesion, name='iniciar_sesion'),
    path('users/create/', user_create, name='user_create'),
    path('reserva/', reserva_create, name='reserva_create'),
    path('lista_reservas/', lista_reservas, name='lista_reservas'),
    path('eliminar_reserva/<int:reserva_id>/', eliminar_reserva, name='eliminar_reserva'),
    path('',inicio, name='inicio'),
    path('perfil/', perfil, name='perfil'),

    
]

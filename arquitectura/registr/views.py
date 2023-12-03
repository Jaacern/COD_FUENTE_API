from .forms import CreateUserForm
from .forms import LoginForm, ReservaForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .models import reserva
import requests
from django.core.mail import send_mail
from django.conf import settings


def registro_usuario(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CreateUserForm()

    return render(request, "registro.html", {"form": form})


def iniciar_sesion(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
                return redirect("perfil")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def user_create(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_list")
        
    else:
        form = UserCreationForm()
    return render(request, "user_create.html", {"form": form})


def reserva_create(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            nueva_reserva = form.save(commit=False)
            nueva_reserva.save()
            send_mail(
                "Reserva creada exitosamente",
                f"Su reserva ha sido creada exitosamente. Detalles de la reserva:\nFecha: {nueva_reserva.fecha}\n",
                nueva_reserva.correo,  
                ["c034eb8f6e5f40@inbox.mailtrap.io"],
                fail_silently=False,
            )
            HttpResponseRedirect(reverse("lista_reservas"))

            # Verificar si la fecha es feriado
            if es_feriado(nueva_reserva.fecha):
                nueva_reserva.delete()  # Eliminar la reserva creada si es un día feriad

    else:
        form = ReservaForm()

    return render(request, "reservar_hora.html", {"form": form})


# envio de correo


# delete
def eliminar_reserva(request, reserva_id):
    # Obtenemos la reserva a eliminar
    reserva_a_eliminar = reserva.objects.filter(id_reserva=reserva_id)
    if reserva_a_eliminar.exists():
        for reserva_a_eliminar in reserva_a_eliminar:
            reserva_a_eliminar.delete()
            return HttpResponseRedirect(reverse("inicio"))

    if request.method == "POST":
        # Confirmación de eliminación
        reserva_a_eliminar.delete()
        # Redirigir a la página principal o a donde prefieras
        return HttpResponseRedirect(reverse("iniciar_sesion"))

    # Mostrar detalles de la reserva antes de confirmar la eliminación
    return render(request, "eliminar_reserva.html", {"reserva": reserva_a_eliminar})


def lista_reservas(request):
    reservas = reserva.objects.all()
    return render(request, "lista_reservas.html", {"reservas": reservas})


# api feriados
def es_feriado(fecha):
    fecha_str = fecha.strftime("%Y-%m-%d")
    url = "https://api.victorsanmartin.com/feriados/en.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        feriados_data = response.json().get(
            "data", []
        )  # Obtiene la lista de feriados del objeto JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener feriados: {e}")
        return False

    for feriado in feriados_data:
        if feriado.get("date") == fecha_str:
            return True

    return False


def inicio(request):
    return render(request, "inicio.html")

def perfil(request):
    return render(request, "perfil.html")
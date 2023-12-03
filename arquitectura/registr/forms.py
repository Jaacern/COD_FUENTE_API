from django import forms
from .models import Usuario, reserva


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rut', 'email', 'username']
        labels = {
            'rut': 'RUT',
            'email': 'Correo electrónico',
            'username': 'Nombre de usuario',
        }



class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    
    

class ReservaForm(forms.ModelForm):
    class Meta:
        model = reserva
        fields = ['id_reserva', 'rut', 'fecha', 'hora', 'medico', 'correo']
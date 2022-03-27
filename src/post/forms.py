from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
        }
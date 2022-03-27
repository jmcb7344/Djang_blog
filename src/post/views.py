from django.contrib.auth.models import User
from django.urls import reverse_lazy
from post import forms
from django.views import generic
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #solo se creo para prueba
    
    return HttpResponse('hola', 'base.html')

class NuevoUser(generic.CreateView):
    model = User
    template_name = 'registration/registro.html'
    form_class = forms.RegistroForm
    success_url = reverse_lazy('login')
    
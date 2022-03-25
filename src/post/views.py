from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #solo se creo para prueba
    
    return HttpResponse('hola', 'base.html')
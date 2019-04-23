from django.shortcuts import render
from .funciones import source
import unittest
from unittest.mock import Mock,MagicMock

from django.http import HttpResponse
from django.conf.urls import url
# Create your views here.


#Falla al principio no deberia mostrar nada
#Cuando no encuentra el usuario no tiene que petar
#Falla el boton de reset

def index(request):
    username = GetUsername(request)
    twitter_obj = source.twitter2(username)

    if username == None:
        word_list = ["Tienes que introducir un username valido"]
    else:
        word_list = twitter_obj.word_count()

    print(username)
    return render(request, 'index.html', {'word_list' : word_list, 'username' : username})

def GetUsername(request):
    return request.GET.get('username')
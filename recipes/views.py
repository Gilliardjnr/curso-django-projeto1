from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Você está na página inicial')


def sobre(request):
    return HttpResponse('Você está na sessão sobre')


def contato(request):
    return HttpResponse('Você está na sessão contatos')
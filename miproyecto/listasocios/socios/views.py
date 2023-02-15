from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    infosocios = loader.get_template('infosocios.html')
    return HttpResponse(infosocios.render())
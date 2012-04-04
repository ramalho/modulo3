# coding: utf-8

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

import datetime

from .models import Pizza

def hora_atual(request):
    agora = datetime.datetime.now()
    html = '<html><body><h1>Hora atual: {0}</h1></body></html>'.format(agora)
    return HttpResponse(html)

def pizzas_pendentes(request):
    lista_de_pizzas = Pizza.objects.all()
    return render(request, 'entrega/pizzas.html', 
                           {"lista": lista_de_pizzas},
                           content_type="text/html")

def pizzas_pendentes_na_unha(request):
    listagem = []
    for pizza in Pizza.objects.all():
        listagem.append(unicode(pizza))
    listagem = u'\n'.join(listagem)    
    html = u'<html><body><h1>Pizzas pendentes</h1>'
    html += u'<pre>{0}</pre></body></html>'.format(listagem)
    return HttpResponse(html)

# coding: utf-8

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

import datetime

from .models import Pizza, Pedido
from .forms import ClienteModelForm, ObservacaoClienteForm

def pizzas_pendentes(request):
    return render(request, 'entrega/pizzas.html', 
                           {"fila": Pizza.objects.all(),
                            "hora": datetime.datetime.now()},
                           content_type="text/html")

class HoraView(TemplateView):
    template_name = 'entrega/hora.html'
    hora_certa = None
    
    def get_context_data(self, **kwargs):
        context = super(HoraView, self).get_context_data(**kwargs)
        context['hora_certa'] = datetime.datetime.now()
        return context

def hora_atual_na_unha(request):
    agora = datetime.datetime.now()
    html = '<html><body><h1>Hora atual: {0}</h1></body></html>'.format(agora)
    return HttpResponse(html)

def pizzas_pendentes_na_unha(request):
    listagem = []
    for pizza in Pizza.objects.all():
        listagem.append(unicode(pizza))
    listagem = u'\n'.join(listagem)    
    html = u'<html><body><h1>Pizzas pendentes</h1>'
    html += u'<pre>{0}</pre></body></html>'.format(listagem)
    return HttpResponse(html)

def hello(request, texto):
    html = '<h1>Hello, %s</h1>' % texto
    return HttpResponse(html)

from django.core.urlresolvers import reverse
    
def cadastro(request):
    if request.method == 'POST':
        formulario = ClienteModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse('lista-clientes'))
    else:
        formulario = ClienteModelForm()
        
    return render(request, 'entrega/cadastro.html',
        {'formulario':formulario})
        
def pedido_pronto(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        pedido = Pedido.objects.get(pk=pedido_id)
        pedido.pronto = True
        pedido.save()
    return HttpResponseRedirect(reverse('lista-pizzas'))
    
def cliente_obs(request):
    if request.method == 'POST':
        formulario = ObservacaoClienteForm(request.POST)
        if formulario.is_valid():
            cliente_id = request.POST.get('cliente_id')
            cliente = Cliente.objects.get(pk=cliente_id)
            cliente.obs = formulario.cleaned_data['obs']
            cliente.save()
    return HttpResponseRedirect(reverse('ficha-cli'))

        
    
    
    
    



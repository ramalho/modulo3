from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView

from .views import HoraView, pizzas_pendentes, hello, cadastro
from .models import Pizza, Cliente

urlpatterns = patterns('',
    #url(r'hora$', hora_atual, name='hora'),
    url(r'hello/(\w+)', hello, name='hello'),
    url(r'hora$', HoraView.as_view(), name='hora'),
    #url(r'pizzas$', pizzas_pendentes, name='pizzas_pendentes'),
    url(r'pizzas$', ListView.as_view(model=Pizza,
                                     context_object_name='lista')),
    url(r'clientes$', ListView.as_view(model=Cliente,
                                     context_object_name='lista'),
                                     name='lista-clientes'),

    url(r'novocli/$', cadastro, name='cadastro-novo'),
    url(r'cli/(?P<pk>\d+)$', 
        DetailView.as_view(model=Cliente, context_object_name='cli'),
        name='ficha-cli'),
)

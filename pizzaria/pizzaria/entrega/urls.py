from django.conf.urls import patterns, include, url

from .views import hora_atual, pizzas_pendentes

urlpatterns = patterns('',
    url(r'hora$', hora_atual, name='hora'),
    url(r'pizzas$', pizzas_pendentes, name='pizzas_pendentes'),
)

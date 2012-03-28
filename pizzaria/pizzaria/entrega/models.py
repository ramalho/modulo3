# coding: utf-8

from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=128, db_index=True)
    fone = models.CharField(max_length=16, db_index=True)
    ramal = models.CharField(max_length=4, blank=True)
    email = models.EmailField(blank=True)
    logradouro = models.CharField(max_length=32, db_index=True)
    numero = models.PositiveIntegerField(u'número')
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(u'observação', blank=True)
    
    class Meta:
        unique_together = ('fone', 'ramal')
        
    def __unicode__(self):
        return self.nome
        
    def endereco(self):
        return u'%s, %s' % (self.logradouro, self.numero)
    endereco.short_description = u'Endereço'

class Pedido(models.Model):
    inclusao = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    pronto = models.BooleanField(default=False)
    entregador = models.ForeignKey('Entregador', null=True, blank=True)
    partida = models.TimeField(null=True, blank=True)

class Entregador(models.Model):
    nome = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.nome
        
    class Meta:
        verbose_name_plural = u'Entregadores'
    











		
		


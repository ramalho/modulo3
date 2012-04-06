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
        ordering = ['fone', 'ramal']
        
    @models.permalink
    def get_absolute_url(self):
        #return '/ent/cli/%s' % self.id
        return ('ficha-cli', (), {'pk':self.id})
        
    def __unicode__(self):
        fone = self.fone
        if self.ramal:
            fone += ' r.' + self.ramal
        return fone + '-' + self.nome
        
    def endereco(self):
        return u'%s, %s' % (self.logradouro, self.numero)
    endereco.short_description = u'Endereço'

class Pedido(models.Model):
    inclusao = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    pronto = models.BooleanField(default=False)
    entregador = models.ForeignKey('Entregador', null=True, blank=True)
    partida = models.TimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.inclusao.strftime('%H:%M') + ' - ' + self.cliente.nome

class Entregador(models.Model):
    nome = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.nome
        
    class Meta:
        verbose_name_plural = u'Entregadores'

SABORES = [
    ('mussarela', 'Mussarela'),
    ('portuguesa', 'Portuguesa'),
    ('calabresa', 'Calabresa'),
    ('atum', 'Atum'),
]
    
class Pizza(models.Model):
    pedido = models.ForeignKey(Pedido)
    sabor1 = models.CharField(u'sabor 1', max_length=32, choices=SABORES)
    coberto1 = models.BooleanField(u'cob.')
    sabor2 = models.CharField(u'sabor 2', max_length=32, choices=SABORES, blank=True)
    coberto2 = models.BooleanField(u'cob.')
    obs = models.TextField(u'observação', blank=True) 

    def __unicode__(self):
        sabor = self.sabor1
        if self.coberto1:
            sabor += ' coberta'
        if self.sabor2:
            sabor2 = self.sabor2    
            if self.coberto2:
                sabor2 += ' coberta'
            sabor = u'½ %s, ½ %s' % (sabor, sabor2)
        return sabor
            






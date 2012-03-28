# coding: utf-8

from django.contrib import admin

from .models import Cliente, Pedido, Entregador

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = ('fone', 'nome')
    search_fields = ['fone', 'nome', 'logradouro', 'numero']
    list_filter = ('logradouro',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'cliente', 'pronto', 'partiu')
    
    def hora_inclusao(self, obj):
        return obj.inclusao.strftime('%H:%M')
        
    def partiu(self, obj):
        return bool(obj.pronto and obj.entregador and obj.partida)
    partiu.boolean = True
    
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)

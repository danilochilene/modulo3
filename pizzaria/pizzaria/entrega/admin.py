# coding: utf-8
from django.contrib import admin
from .models import Cliente, Pedido, Entregador

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', u'endereco')
    search_fields = ['fone', 'nome', 'logradouro']
    list_display_links = list_display
    list_filter = ('logradouro',)    

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'entregador', u'cliente', 'pronto', 'partiu')
    
    def hora_inclusao(self, obj):
        return obj.inclusao.strftime('%H:%M')

    def partiu(self, obj):
        return bool(obj.pronto and obj.entregador and obj.partida)
    partiu.boolean = True
  
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)
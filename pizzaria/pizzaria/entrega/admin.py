from models import Cliente, Pedido, Entregador, Pizza
from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ('fone', 'logradouro', 'email', 'nome')
    list_filter = ['logradouro']

class PizzaAdmin(admin.TabularInline):
    model = Pizza
    #exclude = ('obs',)
    formfield_overrides = {
    TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    
class PedidoAdmin(admin.ModelAdmin):
    list_display= ('hora_inclusao', 'cliente', 'pronto', 'Partiu')
    list_select_related = True
    inlines = [PizzaAdmin]
    date_hierarchy= 'inclusao'
    
    def hora_inclusao(self, pedido):
        return pedido.inclusao.strftime('%H:%M')
    
    def Partiu(self, pedido):
        return bool(pedido.pronto and pedido.partida and pedido.entregador)
    Partiu.boolean = True
   
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)


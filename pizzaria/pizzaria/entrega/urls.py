from django.conf.urls import patterns, include, url

from .views import hora_atual, pizzas_pendentes, HoraView, cadastro, pedido_pronto, cliente_obs
from django.views.generic import ListView, DetailView
from .models import Pizza, Cliente

qs_pizzas_nao_prontas = Pizza.objects.filter(pedido__pronto=False).order_by('pedido')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizzaria.views.home', name='home'),
    # url(r'^pizzaria/', include('pizzaria.foo.urls')),
    url(r'hora$', HoraView.as_view(), name='hora'),
    #url(r'pizzas$', pizzas_pendentes, name='pizzas_pendentes'), 
    url(r'pizzas$',ListView.as_view(queryset=qs_pizzas_nao_prontas, model=Pizza, context_object_name='lista'), name='pizzas'),
    url(r'clientes$', ListView.as_view(model=Cliente, context_object_name='clientes'), name='clientes'),
    url(r'cliente/(?P<pk>\d+)$', DetailView.as_view(model=Cliente, context_object_name='cliente'),),
    url(r'novocli/$', cadastro, name='cadastro-novo'),
    url(r'pedido_pronto', pedido_pronto, name='pedido-pronto'),
    url(r'cliente_obs', cliente_obs, name='cliente-obs'),    
)

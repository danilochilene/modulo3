#coding=utf8
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
import datetime
from pizzaria.entrega.models import Pizza, Pedido
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ClienteModelForm, ObservacaoClienteForm
from django.core.urlresolvers import reverse

class HoraView(TemplateView):
    template_name = 'entrega/hora.html'
    
    def get_context_data(self, **kwargs ):
        context = super(HoraView, self).get_context_data(**kwargs)
        context['hora_certa'] = datetime.datetime.now()
        return context

def hora_atual(request):
    agora = datetime.datetime.now()
    html = u'<html><body> Hora atual: {0}</body></html>'.format(agora)
    return HttpResponse(html)
    
def pizzas_pendentes_na_unha(request):
    listagem = []
    for pizza in Pizza.objects.all():
        listagem.append(unicode(pizza))
    html = u'<html><body><h1> Pizzas pendentes </h1>'
    html += u'<pre>{0}</pre></body></html>'.format(',\n'.join(listagem))
    return HttpResponse(html)
    
def pizzas_pendentes(request):
    return render(request, 'entrega/pizzas.html',
                           {"fila": Pizza.objects.order_by('pedido').all(),
                            "hora": datetime.datetime.now()},
                           content_type="text/html")

def cadastro(request):
    if request.method == 'POST':
        formulario = ClienteModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # XXX: trocar URL por home
            return HttpResponseRedirect(reverse('clientes'))
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
    return HttpResponseRedirect(reverse('pizzas'))
    
def cliente_obs(request):
    if request.method == 'POST':
        formulario = ObservacaoClienteForm(request.POST)
        if formulario.is_valid():
            cliente_id = request.POST.get('cliente_id')
            cliente = Cliente.objects.get(pk=cliente_id)
            cliente.obs = formulario.cleaned_data['obs']
            cliente.save()
        return HttpResponseRedirect(reverse('ficha-cliente'))

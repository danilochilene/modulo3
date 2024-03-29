from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pizzaria.entrega.views import hora_atual

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizzaria.views.home', name='home'),
    # url(r'^pizzaria/', include('pizzaria.foo.urls')),
    url(r'^entrega', include('pizzaria.entrega.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

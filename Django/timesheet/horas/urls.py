from django.conf.urls.defaults import *
#from django.views.generic.simple import direct_to_template
    
urlpatterns = patterns('horas.views',
(r'lista$', 'lista'),
#(r'projetos/$', direct_to_template, {'template': 'projetos_index.html'}),
(r'lancamento/(?P<lanc_id>\d+)/$', 'detalhe'),
(r'lanca/$', 'lanca'),
(r'lanca/(?P<lanc_id>\d+)/$', 'lanca'),
)
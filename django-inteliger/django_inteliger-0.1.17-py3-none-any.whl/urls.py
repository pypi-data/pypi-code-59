from django.urls import re_path, include
from core.views import InteligerView

urlpatterns = [
    re_path(r'cliente/', include(('cliente.urls', 'core.cliente'), namespace='cliente')),
    re_path(r'filial/', include(('filial.urls', 'core.filial'), namespace='filial')),
    re_path(r'fornecedor/', include(('fornecedor.urls', 'core.fornecedor'), namespace='fornecedor')),
    re_path(r'funcionario/', include(('cliente.urls', 'core.cliente'), namespace='cliente')),
    re_path(r'log/', include(('log.urls', 'core.log'), namespace='log')),
    re_path(r'produto/', include(('produto.urls', 'core.produto'), namespace='produto')),
    re_path(r'sistema/', include(('sistema.urls', 'core.sistema'), namespace='sistema')),
    re_path(r'usr/', include(('usr.urls', 'core.usr'), namespace='usr')),

    re_path(r'atualizar$', InteligerView.as_view(), name='sistema_atualizar'),
]

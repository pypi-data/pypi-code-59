from django.urls import re_path, include
from core.views import InteligerView

urlpatterns = [
    re_path(r'cliente/', include(('cliente.urls', 'cliente'), namespace='cliente')),
    re_path(r'filial/', include(('filial.urls', 'filial'), namespace='filial')),
    re_path(r'fornecedor/', include(('fornecedor.urls', 'fornecedor'), namespace='fornecedor')),
    re_path(r'funcionario/', include(('cliente.urls', 'cliente'), namespace='cliente')),
    re_path(r'log/', include(('log.urls', 'log'), namespace='log')),
    re_path(r'produto/', include(('produto.urls', 'produto'), namespace='produto')),
    re_path(r'sistema/', include(('sistema.urls', 'sistema'), namespace='sistema')),
    re_path(r'usr/', include(('usr.urls', 'usr'), namespace='usr')),

    re_path(r'atualizar$', InteligerView.as_view(), name='sistema_atualizar'),
]

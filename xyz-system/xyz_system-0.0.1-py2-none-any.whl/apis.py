# -*- coding:utf-8 -*-

from . import models, serializers

from rest_framework import viewsets, decorators, response
from xyz_restful.decorators import register

__author__ = 'denishuang'


@register()
class SystemViewSet(viewsets.GenericViewSet):
    queryset = models.System.objects.all()
    serializer_class = serializers.SystemSerializer

    @decorators.list_route(['get'])
    def current(self, request):
        serializer = self.get_serializer_class()(self.get_queryset().first())
        return response.Response(serializer.data)


@register()
class SystemViewSet(viewsets.ModelViewSet):
    queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer



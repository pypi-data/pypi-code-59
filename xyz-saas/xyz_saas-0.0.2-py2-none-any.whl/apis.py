# -*- coding:utf-8 -*-

from . import models, serializers

from rest_framework import viewsets, decorators, response
from xyz_restful.decorators import register

__author__ = 'denishuang'


@register()
class PartyViewSet(viewsets.ModelViewSet):
    queryset = models.Party.objects.all()
    serializer_class = serializers.PartySerializer

    def get_permissions(self):
        party = self.queryset.first()
        if not party:
            return []
        return super(PartyViewSet, self).get_permissions()

    @decorators.list_route(['GET'], permission_classes=[])
    def current(self, request):
        party = models.Party.objects.first()
        data = self.get_serializer(party).data
        return response.Response(data)

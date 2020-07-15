# -*- coding:utf-8 -*-

__author__ = 'denishuang'
from . import models, serializers, stats
from rest_framework import viewsets, decorators
from xyz_restful.decorators import register
from xyz_util.statutils import do_rest_stat_action


@register()
class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    search_fields = ('name', 'code')
    filter_fields = {
        'id': ['exact', 'in'],
        'is_active': ['exact'],
        'name': ['exact'],
        'category': ['exact'],
        'code': ['exact']
    }
    ordering_fields = ('is_active', 'title', 'create_time')

    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_course)


@register()
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    search_fields = ('name', 'code')
    filter_fields = ('code', 'name')


@register()
class ChapterViewSet(viewsets.ModelViewSet):
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
    search_fields = ('name', 'code')
    filter_fields = {
        'id': ['exact', 'in'],
        'course': ['exact']
    }

# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from xyz_restful.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models


class CourseSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Course
        exclude = ()
        read_only_fields = ('user', )


class TransactionSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        exclude = ()
        read_only_fields = ('user', )


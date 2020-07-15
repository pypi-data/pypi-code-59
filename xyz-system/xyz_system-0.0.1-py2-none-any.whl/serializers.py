# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from rest_framework import serializers
from . import models


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.System
        fields = '__all__'

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Master
        fields = '__all__'

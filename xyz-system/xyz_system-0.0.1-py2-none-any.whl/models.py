# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from xyz_util.modelutils import JSONField

class System(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "系统"

    name = models.CharField("名称", max_length=64)
    logo = models.URLField("Logo地址", blank=True, null=True)
    role_model_map = JSONField("角色权限", blank=True, default={})
    settings = JSONField("配置")

    def __unicode__(self):
        return self.name

class Master(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "管理员"

    user = models.OneToOneField(User, verbose_name=User._meta.verbose_name,  related_name="as_system_master")

    def __unicode__(self):
        return self.name



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 14:52
# @Author  : Neil.tang
# @Site    : 
# @File    : models.py
# @Software: PyCharm
#
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class System(models.Model):
    Id = models.AutoField(
        primary_key=True,
        verbose_name='系统ID'
    )
    Name = models.CharField(
        verbose_name='系统名称',
        max_length=255,
        unique=True
    )
    CreateTime = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )
    ChangeTime = models.DateTimeField(
        verbose_name='修改时间',
        auto_now=True
    )
    Note = models.TextField(
        verbose_name='备注',
        max_length=255,
        unique=False
    )
    class Meta:
        default_permissions = []
        permissions = (
            ('view_system', '可以查看系统列表'),
            ('add_system', '可以添加系统'),
            ('change_system', '可以编辑系统'),
            ('delete_system', '可以删除系统'),
        )
    def __unicode__(self):
        return '%s' % (self.Name)
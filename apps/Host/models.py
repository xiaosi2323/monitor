#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 14:52
# @Author  : Neil.tang
# @Site    : 
# @File    : models.py
# @Software: PyCharm
#
from __future__ import unicode_literals
from System.models import System
from django.db import models

# Create your models here.
class Host(models.Model):
    Id = models.AutoField(
        primary_key=True,
        verbose_name='主机ID'
    )
    Name = models.CharField(
        verbose_name='主机名称',
        max_length=255
    )
    Ip = models.CharField(
        verbose_name='主机IP',
        max_length=255
    )
    Status = models.CharField(
        verbose_name='状态',
        max_length = 255
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
        null=True
    )
    class Meta:
        default_permissions = []
        permissions = (
            ('view_host', '可以查看主机'),
            ('add_host', '可以添加主机'),
            ('change_host', '可以编辑主机'),
            ('delete_host', '可以删除主机'),
        )

    def __unicode__(self):
        return '%s' % (self.Name)
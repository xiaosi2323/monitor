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
from Host.models import Host
from django.db import models

# Create your models here.

class Databases(models.Model):
    Id = models.AutoField(
        primary_key=True,
        verbose_name='数据库ID'
    )
    Name = models.CharField(
        verbose_name='数据库名称',
        max_length=255,
        unique=True
    )
    SystemId = models.ForeignKey(
        verbose_name='系统Id',
        to=System,
        null=True,
        blank=False
    )
    HostId = models.ManyToManyField(
        verbose_name='主机Id',
        to=Host
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
            ('view_databases', '可以查看数据库'),
            ('add_databases', '可以添加数据库'),
            ('change_databases', '可以编辑数据库'),
            ('delete_databases', '可以删除数据库'),
        )

    def __unicode__(self):
        return '%s' % (self.Name)


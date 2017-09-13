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

class Network(models.Model):
    Id = models.AutoField(
        primary_key=True,
        verbose_name='网络ID'
    )
    DC = models.CharField(
        verbose_name='数据中心',
        max_length=255,
        unique=True
    )
    Name = models.CharField(
        verbose_name='网络名称',
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
        null=True
    )
    class Meta:
        default_permissions = []
        permissions = (
            ('view_network', '可以查看网络'),
            ('add_network', '可以添加网络'),
            ('change_network', '可以编辑网络'),
            ('delete_network', '可以删除网络'),
        )

    def __unicode__(self):
        return '%s' % (self.Name)


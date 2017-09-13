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


# Django表结构

class Menus(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'菜单名')
    parent = models.ForeignKey('self',
                               verbose_name=u'父级菜单',
                               null=True,
                               blank=True,
                               default='0',
                               help_text=u'如果添加的是子菜单，请选择父菜单')
    show = models.BooleanField(verbose_name=u'是否显示',
                               default=False,
                               help_text=u'菜单是否显示，默认添加不显示')
    url = models.CharField(max_length=300,
                           verbose_name=u'菜单url地址',
                           null=True,
                           blank=True,
                           default='javascript:void(0)',
                           help_text=u'是否给菜单设置一个url地址')
    priority = models.IntegerField(verbose_name=u'显示优先级',
                                   null=True,
                                   blank=True,
                                   default=-1,
                                   help_text=u'菜单的显示顺序，优先级越大显示越靠前')
    permission_id = models.CharField(verbose_name=u'权限编号',
                                     max_length=250,
                                     help_text=u'给菜单设置一个编号，用于权限控制',
                                     error_messages={'field-permission_id': u'输入权限'})

    def __str__(self):
        return "{parent}{name}".format(name=self.name, parent=u"%s-->" % self.parent.name if self.parent else '')

    class Meta:
        verbose_name = u"菜单"
        verbose_name_plural = u"菜单"
        ordering = ["-priority", "id"]

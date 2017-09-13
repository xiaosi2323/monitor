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
class Business(models.Model):
    class Meta:
        default_permissions = []
        permissions = (
            ('view_business', '查看业务指标'),
        )
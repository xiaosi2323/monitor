#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:01
# @Author  : Neil.tang
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from rest_framework import viewsets,filters
from models import System
from serializers import SystemSerializers
from syn import get_monitor_info
from django.http import HttpResponse
from django.contrib.auth.views import login_required

@login_required
def SynSystem(req):
    list = []
    for x in get_monitor_info():
        if  System.objects.filter(Name=x['name']).exists():
            list.append(u'%s,已存在<br/>'%x['name'])
        else:
            list.append(u'%s,添加成功<br/>'%x['name'])
            p = System(Name=x['name'])
            p.save()
    return HttpResponse(list)

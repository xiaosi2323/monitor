#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:01
# @Author  : Neil.tang
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from models import Host
from syn import get_monitor_info
from django.http import HttpResponse
from django.contrib.auth.views import login_required

@login_required
def SynHost(req):
    list = []
    for x in get_monitor_info():
        if  Host.objects.filter(Ip=x['ip']).exists():
            list.append(u'%s,已存在<br/>'%x['ip'])
        else:
            list.append(u'%s,添加成功<br/>'%x['ip'])
            p = Host(Name=x['hostname'],Ip=x['ip'],Status=x['status'])
            p.save()
    return HttpResponse(list)
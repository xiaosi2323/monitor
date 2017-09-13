#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:01
# @Author  : Neil.tang
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from django.views.generic import TemplateView

class ConfigSystemView(TemplateView):
    template_name = 'monitor/system.html'

class ConfigAppView(TemplateView):
    template_name = 'monitor/app.html'

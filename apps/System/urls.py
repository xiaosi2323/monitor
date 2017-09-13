#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 13:35
# @Author  : Neil.tang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from views import SynSystem

urlpatterns = [
    url(r'sync/$',SynSystem)
]
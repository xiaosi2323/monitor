#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 13:39
# @Author  : Neil.tang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from api_views import HostListView


urlpatterns = [
    url(r'list',HostListView.as_view())
]
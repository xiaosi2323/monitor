#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 10:27
# @Author  : Neil.tang
# @Site    : 
# @File    : api_urls.py
# @Software: PyCharm

from django.conf.urls import url
from api_views import SystemHostApi,SystemListApi,SystemDetailApi,SystemCreateApi

urlpatterns = [
    url(r'host/',SystemHostApi.as_view()),
    url(r'list/',SystemListApi.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', SystemDetailApi.as_view()),
    url(r'create/',SystemCreateApi.as_view())
]
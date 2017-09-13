#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 10:27
# @Author  : Neil.tang
# @Site    : 
# @File    : api_urls.py
# @Software: PyCharm

from django.conf.urls import url
from api_views import DatabaseDetailApi,DatabaseListApi

urlpatterns = [
    url(r'list/',DatabaseListApi.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DatabaseDetailApi.as_view()),
]
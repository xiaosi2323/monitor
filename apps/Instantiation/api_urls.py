#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 13:39
# @Author  : Neil.tang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from api_views import InstanListApi,InstanmDetailApi

urlpatterns = [
    url(r'list/$',InstanListApi.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', InstanmDetailApi.as_view()),

]
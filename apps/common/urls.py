#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 13:35
# @Author  : Neil.tang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from views import LoginView, IndexView, LogoutView

urlpatterns = [
    url(r"^login/", LoginView.as_view()),
    url(r"^logout/", LogoutView.as_view(),name="common.logout"),
    url(r'^$', IndexView.as_view(),name="common.index")
]
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 12:50
# @Author  : Neil.tang
# @Site    : 
# @File    : api_urls.py
# @Software: PyCharm
from views import ReportsStatusApplicationView,ReportsStatusDatabasesView,\
    ReportsStatusNetworkView,ReportsStatusSecurityView

from django.conf.urls import url


urlpatterns = [
    url(r"^status/application/",ReportsStatusApplicationView.as_view()),
    url(r"^status/databases/",ReportsStatusDatabasesView.as_view()),
    url(r"^status/security/",ReportsStatusSecurityView.as_view()),
    url(r"^status/network/",ReportsStatusNetworkView.as_view()),
]
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 13:39
# @Author  : Neil.tang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from api_views import ExpressBillApi, ExpressOrderApi,\
    TruckBillApi,TruckOrderApi,ExpressLoadApi,\
    ExpressUnLoadApi,TruckLoadApi,TruckUnLoadApi,BusinessIndexApi

urlpatterns = [
    url(r'index', BusinessIndexApi.as_view()),
    url(r'express/bill', ExpressBillApi.as_view()),
    url(r'express/order', ExpressOrderApi.as_view()),
    url(r'express/load', ExpressLoadApi.as_view()),
    url(r'express/unload', ExpressUnLoadApi.as_view()),
    url(r'truck/bill', TruckBillApi.as_view()),
    url(r'truck/order', TruckOrderApi.as_view()),
    url(r'truck/load', TruckLoadApi.as_view()),
    url(r'truck/unload', TruckUnLoadApi.as_view())
]

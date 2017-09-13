#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 11:35
# @Author  : Neil.tang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from views import BusinessExpressBillView,BusinessExpressLoadView,\
    BusinessExpressOrderView,BusinessExpressUnloadView,\
    BusinessTruckBillView,BusinessTruckLoadView,\
    BusinessTruckOrderView,BusinessTruckUnloadView
urlpatterns = [
    # url(r'index', BusinessIndexApi.as_view()),
    url(r'express/bill', BusinessExpressBillView.as_view()),
    url(r'express/order', BusinessExpressOrderView.as_view()),
    url(r'express/load', BusinessExpressLoadView.as_view()),
    url(r'express/unload', BusinessExpressUnloadView.as_view()),
    url(r'truck/bill', BusinessTruckBillView.as_view()),
    url(r'truck/order', BusinessTruckOrderView.as_view()),
    url(r'truck/load', BusinessTruckLoadView.as_view()),
    url(r'truck/unload', BusinessTruckUnloadView.as_view())
]

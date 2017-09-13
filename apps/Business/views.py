#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 09:13
# @Author  : Neil.tang
# @Site    : 
# @File    : adminlte.py
# @Software: PyCharm
from django.views.generic import View
from django.shortcuts import render, redirect

class BusinessExpressBillView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'express/bill.html')

class BusinessExpressOrderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'express/order.html')

class BusinessExpressLoadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'express/load.html')

class BusinessExpressUnloadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'express/unload.html')

class BusinessTruckBillView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'truck/bill.html')

class BusinessTruckOrderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'truck/order.html')

class BusinessTruckLoadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'truck/load.html')

class BusinessTruckUnloadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'truck/unload.html')


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/22 09:13
# @Author  : Neil.tang
# @Site    : 
# @File    : adminlte.py
# @Software: PyCharm
from django.views.generic import View
from django.shortcuts import render
from django.http.response import HttpResponseForbidden

class ReportsStatusApplicationView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('Reports.view_reports'):
            return HttpResponseForbidden()

        return render(request, 'application/index.html')


class ReportsStatusDatabasesView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('Reports.view_reports'):
            return HttpResponseForbidden()

        return render(request, 'databases/index.html')

class ReportsStatusNetworkView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('Reports.view_reports'):
            return HttpResponseForbidden()

        return render(request, 'network/index.html')


class ReportsStatusSecurityView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('Reports.view_reports'):
            return HttpResponseForbidden()

        return render(request, 'security/index.html')


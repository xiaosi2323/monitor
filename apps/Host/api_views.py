#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:01
# @Author  : Neil.tang
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from rest_framework import viewsets,generics,views
from rest_framework.response import Response
from models import Host
from serializers import HostSerializers

class HostListView(generics.ListAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializers
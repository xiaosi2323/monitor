#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 10:27
# @Author  : Neil.tang
# @Site    : 
# @File    : api_views.py
# @Software: PyCharm

from rest_framework.response import Response
from rest_framework import generics,views, filters
from django.http import Http404
from models import System
from rest_framework import filters
from Instantiation.models import Instantiation
from serializers import SystemSerializers
import django_filters

class SystemListApi(generics.ListAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('Name','Id')
    search_fields = ('Name', 'Id')

class SystemCreateApi(generics.CreateAPIView):
     queryset = System.objects.all()
     serializer_class = SystemSerializers

class SystemDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializers


class SystemHostApi(views.APIView):
    queryset = System.objects.all()
    def get(self,request):
        data = []
        inst = Instantiation.objects.filter(SystemId__Name=request.query_params['system'])
        for row in inst:
            if row.HostId.exists():
                for host in row.HostId.all():
                    data.append({'HostName':host.Name,'HostAddress':host.Ip})
        return Response(data)
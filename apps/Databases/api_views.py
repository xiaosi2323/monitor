#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 10:27
# @Author  : Neil.tang
# @Site    : 
# @File    : api_views.py
# @Software: PyCharm

from rest_framework import generics
from models import Databases
from rest_framework import filters
from serializers import DatabaseSerializers
import django_filters

class DatabaseListApi(generics.ListAPIView):
    queryset = Databases.objects.all()
    serializer_class = DatabaseSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('Name','Id')
    search_fields = ('Name', 'Id')


class DatabaseDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Databases.objects.all()
    serializer_class = DatabaseSerializers


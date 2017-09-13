# -*- coding:utf-8 -*-
from rest_framework import generics,filters
from rest_framework.response import Response
from serializers import InstanSerializer
from models import Instantiation
import django_filters.rest_framework

# 通过实例，或者主机确认系统名的方法
class InstanListApi(generics.ListAPIView):
    queryset = Instantiation.objects.all()
    serializer_class = InstanSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('Name','Id','SystemId__Id','HostId__Ip')
    search_fields = ('Name', 'Id')

class InstanmDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instantiation.objects.all()
    serializer_class = InstanSerializer
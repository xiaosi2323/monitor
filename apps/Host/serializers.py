#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 16:45
# @Author  : Neil.tang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from models import Host


# 序列化
class HostSerializers(serializers.Serializer):
    Id = serializers.IntegerField(label='主机ID',read_only=True)
    Name = serializers.CharField(label='主机名称',required=True)
    Ip = serializers.CharField(label='IP')
    Status = serializers.CharField(label='状态')
    CreateTime = serializers.DateTimeField(label='创建时间',format='%Y-%m-%d %H:%M:%S',read_only=True)
    ChangeTime = serializers.DateTimeField(label='修改时间',format='%Y-%m-%d %H:%M:%S',read_only=True)
    Note = serializers.CharField(label='备注',required=False,allow_blank=True)
    class Meta:
        model = Host
        fields = '__all__'
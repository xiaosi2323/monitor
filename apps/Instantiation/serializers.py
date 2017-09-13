#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 16:45
# @Author  : Neil.tang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from models import Instantiation
from System.serializers import SystemSerializers
from Host.serializers import HostSerializers
# 序列化

class InstanSerializer(serializers.ModelSerializer):
    HostId = HostSerializers(many=True)
    CreateTime = serializers.DateTimeField(label='创建时间',format='%Y-%m-%d %H:%M:%S',read_only=True)
    ChangeTime = serializers.DateTimeField(label='修改时间',format='%Y-%m-%d %H:%M:%S',read_only=True)
    SystemId = SystemSerializers()
    class Meta:
        model = Instantiation
        fields = '__all__'
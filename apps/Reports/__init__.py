#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/24 16:02
# @Author  : Neil.tang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from django.utils.module_loading import autodiscover_modules
default_app_config = 'Reports.apps.TypeConfig'

def autodiscover():
    autodiscover_modules('adminltes')


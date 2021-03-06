#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/10 09:09
# @Author  : Neil.tang
# @Site    : 
# @File    : permissions.py
# @Software: PyCharm
from rest_framework.permissions import DjangoModelPermissions


class DjangoModelViewPermissions(DjangoModelPermissions):
    """
    Create our own permissions class to account for the custom "view" permission
    that needs to be created on any of our models.
    """

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

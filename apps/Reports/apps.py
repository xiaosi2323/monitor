# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class TypeConfig(AppConfig):
    name = 'Reports'

    def ready(self):
        self.module.autodiscover()
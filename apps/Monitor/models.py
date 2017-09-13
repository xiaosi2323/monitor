# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class McObjectClass(models.Model):
    Id = models.AutoField(
        verbose_name='监控类Id',
        primary_key=True,
    )
    Name = models.CharField(
        verbose_name='监控类名称',
        max_length=255,
        unique=True
    )
    CreateTime = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )
    ChangeTime = models.DateTimeField(
        verbose_name='修改时间',
        auto_now=True
    )

    class Meta:
        default_permissions = []

    def __unicode__(self):
        return '%s' % (self.Name)

class McObject(models.Model):
    Id = models.AutoField(
        verbose_name='监控对象Id',
        primary_key=True,
    )
    Name = models.CharField(
        verbose_name='监控对象名称',
        max_length=255
    )
    CreateTime = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )
    ChangeTime = models.DateTimeField(
        verbose_name='修改时间',
        auto_now=True
    )

    class Meta:
        default_permissions = []

    def __unicode__(self):
        return '%s' % (self.Name)

class McParameter(models.Model):
    Id = models.AutoField(
        verbose_name='监控参数Id',
        primary_key=True,
    )
    Name = models.CharField(
        verbose_name='监控参数名称',
        max_length=255,
        unique=True
    )
    CreateTime = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )
    ChangeTime = models.DateTimeField(
        verbose_name='修改时间',
        auto_now=True
    )

    class Meta:
        default_permissions = []

    def __unicode__(self):
        return '%s' % (self.Name)

class Items(models.Model):
    Id = models.AutoField(
        verbose_name='监控详情Id',
        primary_key=True,
    )
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    McObjectClassId = models.ForeignKey(verbose_name='对象类', to=McObjectClass)
    McObjectId = models.ForeignKey(verbose_name='对象类', to=McObject)
    McParameterId = models.ForeignKey(verbose_name='参数', to=McParameter)
    ItemValue = models.CharField(verbose_name='值', max_length=250)
    ItemValueUnit = models.CharField(verbose_name='单位', max_length=250)
    OccurrenceTime = models.DateTimeField(
        verbose_name='发生时间',
        auto_now_add=True
    )
    CreateTime = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )
    class Meta:
        default_permissions = []



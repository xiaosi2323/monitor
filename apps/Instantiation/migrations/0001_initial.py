# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Host', '0001_initial'),
        ('System', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instantiation',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u5b9e\u4f8bID')),
                ('Name', models.CharField(max_length=255, unique=True, verbose_name='\u5b9e\u4f8b\u540d\u79f0')),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('ChangeTime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('Note', models.TextField(max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'default_permissions': [],
                'permissions': (('view_instantiation', '\u53ef\u4ee5\u67e5\u770b\u5b9e\u4f8b'), ('add_instantiation', '\u53ef\u4ee5\u6dfb\u52a0\u5b9e\u4f8b'), ('change_instantiation', '\u53ef\u4ee5\u7f16\u8f91\u5b9e\u4f8b'), ('delete_instantiation', '\u53ef\u4ee5\u5220\u9664\u5b9e\u4f8b')),
            },
        ),
        migrations.CreateModel(
            name='InstantiationHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HostGroup', models.CharField(max_length=255, verbose_name='\u7cfb\u7edf\u6240\u5c5e\u96c6\u7fa4')),
                ('HostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Host.Host')),
                ('InstantiationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instantiation.Instantiation')),
            ],
        ),
        migrations.AddField(
            model_name='instantiation',
            name='HostId',
            field=models.ManyToManyField(through='Instantiation.InstantiationHost', to='Host.Host', verbose_name='\u4e3b\u673aId'),
        ),
        migrations.AddField(
            model_name='instantiation',
            name='SystemId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='System.System', verbose_name='\u7cfb\u7edfId'),
        ),
    ]
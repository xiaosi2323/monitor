# coding:utf-8

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, filters
from models import McObject, McObjectClass, McParameter, Items
from Databases.models import Databases
from Instantiation.models import Instantiation
from Host.models import Host
from Network.models import Network


# from Network.models import Network
# Create your views here.
#
def ObjectClass(mc_object_class):
    ClassObj = McObjectClass.objects.get_or_create(Name=mc_object_class)
    return ClassObj[0]


def Parameter(mc_parameter):
    Par = McParameter.objects.get_or_create(Name=mc_parameter)
    return Par[0]


def Object(mc_object):
    Obj = McObject.objects.get_or_create(Name=mc_object)
    return Obj[0]


def Item(Obj,ObjectClassId,ObjectId,ParameterId,value,unit,time):
    item = Items(content_type=Obj,
                 McObjectClassId=ObjectClassId,
                 McObjectId=ObjectId,
                 McParameterId=ParameterId,
                 ItemValue=value,
                 ItemValueUnit=unit,
                 OccurrenceTime=time
                 )
    item.save()
    return item


class ItemsApi(views.APIView):
    queryset = Items.objects.all()

    def post(self, request):
        try:
            req = request.data
            ObjectClassId = ObjectClass(req['object_class'])
            ObjectId = Object(req['object'])
            ParameterId = Parameter(req['parameter'])
            try:
                if req['type'] == 'host':
                    host = Host.objects.get_or_create(Ip=req['Ip'])
                    Item(host,ObjectClassId,ObjectId,ParameterId,req['value'],req['unit'],req['time'])
                    return Response('成功')
            except:
                return Response('失败')
            try:
                if req['type'] == 'db':
                    database = Databases.objects.get_or_create(Name=req['db'])
                    Item(database,ObjectClassId,ObjectId,ParameterId,req['value'],req['unit'],req['time'])
                    return Response('成功')
            except:
                return Response('失败')
            try:
                if req['type'] == 'app':
                    application = Instantiation.objects.get_or_create(Name=req['app'])
                    Item(application, ObjectClassId, ObjectId, ParameterId,req['value'],req['unit'],req['time'])
                    return Response('成功')
            except:
                return Response('失败')
            try:
                if req['type'] == 'net':
                    network = Network.objects.get_or_create(DC=req['dc'],Name=req['network'])
                    Item(network, ObjectClassId, ObjectId, ParameterId,req['value'],req['unit'],req['time'])
                    return Response('成功')
            except:
                return Response('失败')
        except:
            return Response('传入参数问题！')

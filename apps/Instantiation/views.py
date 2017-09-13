# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from sync import get_monitor_info
from models import Instantiation,InstantiationHost
from System.models import System
from Host.models import Host

# 通过实例，或者主机确认系统名的方法
def InstantiationSystem(instan,ip):
    inst = Instantiation.objects.filter(Name=instan)
    if inst.exists():
        return inst[0].SystemId
    else:
        host = Host.objects.filter(Ip=ip)
        if host.exists():
            return host[0].SystemId
        return System.objects.get(Name="未收录系统")

class SyncInstantiation(APIView):
    queryset = Instantiation.objects.all()

    def get(self, request):
        try:
            instantiation = get_monitor_info()
            for rows in instantiation:
                # 没有实例就创建
                inst = Instantiation.objects.get_or_create(Name=rows['name'])
                if rows.has_key('businesses'):
                    # 存在系统，就判断是否需要更新或新增
                    if inst[0].SystemId == None or inst[0].SystemId.Name != rows['businesses']['name']:
                        system = System.objects.get_or_create(Name=rows['businesses']['name'])
                        Instantiation.objects.filter(Name=rows['name']).update(SystemId=system[0])
                elif rows.has_key('clusters'):
                    # 判断是否存在集群，如果存在循环出所有集群
                    for deviceList in rows['clusters']:
                        cluster = deviceList['name']
                        # 判断集群中是否有主机， 如果有就循环出所有主机设备
                        if deviceList.has_key('deviceList') and deviceList['deviceList'] != None:
                            for device in deviceList['deviceList']:
                                host = Host.objects.get_or_create(Ip=device['ip'],Name=device['hostname'],Status=device['status'])
                                InstantiationHost.objects.get_or_create(HostId=host[0],InstantiationId=inst[0],HostGroup=cluster)
                else:
                    print rows['name']
        except:
            return Response('失败')
        return Response('成功')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:01
# @Author  : Neil.tang
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Business
from django.db import connections
import sys


class ExpressBillApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''SELECT
                    TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s'),
                    sum(TB_EXPRESS.BS_COUNT)
                FROM
                    TB_EXPRESS
                WHERE
                    TB_EXPRESS.CREATETIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_EXPRESS.CREATETIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s')
                order by TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s') AS time1 , SUM(TB_EXPRESS.BS_COUNT) AS count1
    FROM TB_EXPRESS
    WHERE TB_EXPRESS.CREATETIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_EXPRESS.CREATETIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s') AS  time2, SUM(TB_EXPRESS.BS_COUNT) AS count2
    FROM TB_EXPRESS
    WHERE TB_EXPRESS.CREATETIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_EXPRESS.CREATETIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_EXPRESS.CREATETIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class ExpressOrderApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''SELECT
                    TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s'),
                    sum(TB_D_ORDER_ED.BS_COUNT)
                FROM
                    TB_D_ORDER_ED
                WHERE
                    TB_D_ORDER_ED.CREATETIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_D_ORDER_ED.CREATETIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s')
                order by TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s') AS time1 , SUM(TB_D_ORDER_ED.BS_COUNT) AS count1
    FROM TB_D_ORDER_ED
    WHERE TB_D_ORDER_ED.CREATETIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_D_ORDER_ED.CREATETIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s') AS  time2, SUM(TB_D_ORDER_ED.BS_COUNT) AS count2
    FROM TB_D_ORDER_ED
    WHERE TB_D_ORDER_ED.CREATETIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_D_ORDER_ED.CREATETIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_D_ORDER_ED.CREATETIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class TruckBillApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''SELECT
                    TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s'),
                    sum(tb_Less_than_Truck_Load.BS_COUNT)
                FROM
                    tb_Less_than_Truck_Load
                WHERE
                    tb_Less_than_Truck_Load.CREATETIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND tb_Less_than_Truck_Load.CREATETIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s')
                order by TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s') AS time1 , SUM(tb_Less_than_Truck_Load.BS_COUNT) AS count1
    FROM tb_Less_than_Truck_Load
    WHERE tb_Less_than_Truck_Load.CREATETIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND tb_Less_than_Truck_Load.CREATETIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s') AS  time2, SUM(tb_Less_than_Truck_Load.BS_COUNT) AS count2
    FROM tb_Less_than_Truck_Load
    WHERE tb_Less_than_Truck_Load.CREATETIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND tb_Less_than_Truck_Load.CREATETIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(tb_Less_than_Truck_Load.CREATETIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class TruckOrderApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''SELECT
                    TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s'),
                    sum(TB_D_ORDER_LTTL.BS_COUNT)
                FROM
                    TB_D_ORDER_LTTL
                WHERE
                    TB_D_ORDER_LTTL.CREATETIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_D_ORDER_LTTL.CREATETIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s')
                order by TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s') AS time1 , SUM(TB_D_ORDER_LTTL.BS_COUNT) AS count1
    FROM TB_D_ORDER_LTTL
    WHERE TB_D_ORDER_LTTL.CREATETIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_D_ORDER_LTTL.CREATETIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s') AS  time2, SUM(TB_D_ORDER_LTTL.BS_COUNT) AS count2
    FROM TB_D_ORDER_LTTL
    WHERE TB_D_ORDER_LTTL.CREATETIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_D_ORDER_LTTL.CREATETIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_D_ORDER_LTTL.CREATETIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class ExpressLoadApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''
                SELECT
                    TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s'),
                    sum(TB_EXPRESS_LOAD.WAYBILL_COUNT)
                FROM
                    TB_EXPRESS_LOAD
                WHERE
                    TB_EXPRESS_LOAD.CREATE_TIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_EXPRESS_LOAD.CREATE_TIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s')
                order by TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s') AS time1 , SUM(TB_EXPRESS_LOAD.WAYBILL_COUNT) AS count1
    FROM TB_EXPRESS_LOAD
    WHERE TB_EXPRESS_LOAD.CREATE_TIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_EXPRESS_LOAD.CREATE_TIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s') AS  time2, SUM(TB_EXPRESS_LOAD.WAYBILL_COUNT) AS count2
    FROM TB_EXPRESS_LOAD
    WHERE TB_EXPRESS_LOAD.CREATE_TIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_EXPRESS_LOAD.CREATE_TIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_EXPRESS_LOAD.CREATE_TIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class ExpressUnLoadApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''
                SELECT
                    TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s'),
                    sum(TB_EXPRESS_UNLOAD.WAYBILL_COUNT)
                FROM
                    TB_EXPRESS_UNLOAD
                WHERE
                    TB_EXPRESS_UNLOAD.CREATE_TIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_EXPRESS_UNLOAD.CREATE_TIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s')
                order by TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s') AS time1 , SUM(TB_EXPRESS_UNLOAD.WAYBILL_COUNT) AS count1
    FROM TB_EXPRESS_UNLOAD
    WHERE TB_EXPRESS_UNLOAD.CREATE_TIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_EXPRESS_UNLOAD.CREATE_TIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s') AS  time2, SUM(TB_EXPRESS_UNLOAD.WAYBILL_COUNT) AS count2
    FROM TB_EXPRESS_UNLOAD
    WHERE TB_EXPRESS_UNLOAD.CREATE_TIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_EXPRESS_UNLOAD.CREATE_TIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_EXPRESS_UNLOAD.CREATE_TIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class TruckLoadApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''
                SELECT
                    TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s'),
                    sum(TB_LOAD_UNLOAD.LOAD_COUNT)
                FROM
                    TB_LOAD_UNLOAD
                WHERE
                    TB_LOAD_UNLOAD.CREATETIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_LOAD_UNLOAD.CREATETIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s')
                order by TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s') AS time1 , SUM(TB_LOAD_UNLOAD.LOAD_COUNT) AS count1
    FROM TB_LOAD_UNLOAD
    WHERE TB_LOAD_UNLOAD.CREATETIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_LOAD_UNLOAD.CREATETIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s') AS  time2, SUM(TB_LOAD_UNLOAD.LOAD_COUNT) AS count2
    FROM TB_LOAD_UNLOAD
    WHERE TB_LOAD_UNLOAD.CREATETIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_LOAD_UNLOAD.CREATETIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class TruckUnLoadApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'cg':
                groupby = query['groupby']
                start_time = query['start_time']
                end_time = query['end_time']
                cursor.execute('''
                SELECT
                    TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s'),
                    sum(TB_LOAD_UNLOAD.UNLOAD_COUNT)
                FROM
                    TB_LOAD_UNLOAD
                WHERE
                    TB_LOAD_UNLOAD.CREATETIME >= TO_DATE('%(start_time)s', 'YYYY-MM-DD hh24:mi')
                AND TB_LOAD_UNLOAD.CREATETIME <= TO_DATE('%(end_time)s', 'YYYY-MM-DD hh24:mi')
                GROUP BY
                    TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s')
                order by TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s') asc''' % (
                    {'groupby': groupby, 'start_time': start_time, 'end_time': end_time}))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value'] = row[1]
                    data.append(bill)
                return Response(data)

            # 对比查询
            if query['type'] == 'db':
                groupby = query['t_groupby']
                start_time1 = query['t_start_time1']
                end_time1 = query['t_end_time1']
                start_time2 = query['t_start_time2']
                end_time2 = query['t_end_time2']
                cursor.execute('''
                SELECT NVL(cg.time1, db.time2),NVL(cg.count1,0),NVL(db.count2,0)   FROM (
    SELECT TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s') AS time1 , SUM(TB_LOAD_UNLOAD.UNLOAD_COUNT) AS count1
    FROM TB_LOAD_UNLOAD
    WHERE TB_LOAD_UNLOAD.CREATETIME >= TO_DATE('%(start_time1)s', 'YYYY-MM-DD hh24:mi')
    AND TB_LOAD_UNLOAD.CREATETIME <= TO_DATE('%(end_time1)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s')) cg FULL OUTER JOIN (
    SELECT TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s') AS  time2, SUM(TB_LOAD_UNLOAD.UNLOAD_COUNT) AS count2
    FROM TB_LOAD_UNLOAD
    WHERE TB_LOAD_UNLOAD.CREATETIME >= TO_DATE('%(start_time2)s', 'YYYY-MM-DD hh24:mi')
    AND TB_LOAD_UNLOAD.CREATETIME <= TO_DATE('%(end_time2)s', 'YYYY-MM-DD hh24:mi')
    GROUP BY TO_CHAR(TB_LOAD_UNLOAD.CREATETIME,'%(groupby)s')) db ON cg.time1 = db.time2
    ORDER BY TO_CHAR(db.time2) ASC ;''' % ({
                    'groupby': groupby,
                    'start_time1': start_time1,
                    'start_time2': start_time2,
                    'end_time1': end_time1,
                    'end_time2': end_time2
                }))
                for row in cursor.fetchall():
                    bill = {}
                    bill['key'] = row[0]
                    bill['value1'] = row[1]
                    bill['value2'] = row[2]
                    data.append(bill)
                return Response(data)
            else:
                return Response("选择查询条件！")
        except:
            return Response("访问有误！")

class BusinessIndexApi(APIView):
    queryset = Business.objects.all()

    def get(self, request):
        try:
            data = []
            query = request.GET
            cursor = connections['jkdb'].cursor()
            # 常规查询
            if query['type'] == 'zhibiao':
                cursor.execute(u'''
                    select logistics_currentvalue as 零担今日开单量,
                    logistics_periodvalue	as 零担上周开单量,
                    express_currentvalue	as 快递今日开单量,
                    express_periodvalue	as 快递上周开单量,
                    logistics_currentvalue_user	as 零担今日订单量,
                    logistics_periodvalue_user	as 零担上周订单量,
                    express_currentvalue_user	as 快递今日订单量,
                    express_periodvalue_user	as 快递上周订单量
                    from patrol.v_daily_count@jkdp_to_foss
                ''');
                col_names = cursor.description
                return Response([dict(zip([col[0] for col in col_names], row))
                                 for row in cursor.fetchall()])

            if query['type'] == 'charts':
                if query['name'] == 'Truck_Load_bill':
                    cursor.execute(u'''
                        select NVL(a.time, b.time) as 时间 ,NVL(a.BS_COUNT,0) as 上周同期 ,NVL(b.BS_COUNT,0) as 今日开单  from
(SELECT  TO_CHAR(CREATETIME,'hh24:mi') time,BS_COUNT  from tb_less_than_truck_load where BS_COUNT >='0' and
 CREATETIME >= sysdate - interval '7' day - interval '3' hour  and CREATETIME <= sysdate - interval '7' day
order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) a FULL OUTER JOIN (SELECT  TO_CHAR(CREATETIME,'hh24:mi') time ,BS_COUNT from
tb_less_than_truck_load where BS_COUNT >='0' and  CREATETIME >= sysdate - interval '3' hour
 order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) b  on a.time = b.time
                    ''');
                    for row in cursor.fetchall():
                        bill = {}
                        bill['key'] = row[0]
                        bill['value'] = row[1]
                        bill['value2'] = row[2]
                        data.append(bill)
                    return Response(data)
                if query['name'] == 'express_bill':
                    cursor.execute(u'''select NVL(a.time, b.time) as 时间 ,NVL(a.BS_COUNT,0) as 上周同期 ,NVL(b.BS_COUNT,0) as 今日开单  from
            (SELECT  TO_CHAR(CREATETIME,'hh24:mi') time,BS_COUNT  from TB_EXPRESS where BS_COUNT >='0' and
             CREATETIME >= sysdate - interval '7' day - interval '3' hour  and CREATETIME <= sysdate - interval '7' day
            order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) a FULL OUTER JOIN (SELECT  TO_CHAR(CREATETIME,'hh24:mi') time ,BS_COUNT from
            TB_EXPRESS where BS_COUNT >='0' and  CREATETIME >= sysdate - interval '3' hour
             order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) b  on a.time = b.time''');
                    for row in cursor.fetchall():
                        bill = {}
                        bill['key'] = row[0]
                        bill['value'] = row[1]
                        bill['value2'] = row[2]
                        data.append(bill)
                    return Response(data)
                if query['name'] == 'Truck_Load_order':
                    cursor.execute(u'''select NVL(a.time, b.time) as 时间 ,NVL(a.BS_COUNT,0) as 上周同期 ,NVL(b.BS_COUNT,0) as 今日订单  from
(SELECT  TO_CHAR(CREATETIME,'hh24:mi') time,BS_COUNT  from TB_D_ORDER_LTTL where BS_COUNT >='0' and
 CREATETIME >= sysdate - interval '7' day - interval '3' hour  and CREATETIME <= sysdate - interval '7' day
order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) a FULL OUTER JOIN
(SELECT  TO_CHAR(CREATETIME,'hh24:mi') time ,BS_COUNT from
TB_D_ORDER_LTTL where BS_COUNT >='0' and  CREATETIME >= sysdate - interval '3' hour
 order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) b on a.time = b.time''');
                    for row in cursor.fetchall():
                        bill = {}
                        bill['key'] = row[0]
                        bill['value'] = row[1]
                        bill['value2'] = row[2]
                        data.append(bill)
                    return Response(data)
                if query['name'] == 'express_order':
                    cursor.execute(u'''select NVL(a.time, b.time) as 时间 ,NVL(a.BS_COUNT,0) as 上周同期 ,NVL(b.BS_COUNT,0) as 今日订单  from
(SELECT  TO_CHAR(CREATETIME,'hh24:mi') time,BS_COUNT  from TB_D_ORDER_ED where BS_COUNT >='0' and
 CREATETIME >= sysdate - interval '7' day - interval '3' hour  and CREATETIME <= sysdate - interval '7' day
order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) a FULL OUTER JOIN
(SELECT  TO_CHAR(CREATETIME,'hh24:mi') time ,BS_COUNT from
TB_D_ORDER_ED where BS_COUNT >='0' and  CREATETIME >= sysdate - interval '3' hour
 order by TO_CHAR(CREATETIME,'yyyy-mm-dd hh24:mi')) b on a.time = b.time''');
                    for row in cursor.fetchall():
                        bill = {}
                        bill['key'] = row[0]
                        bill['value'] = row[1]
                        bill['value2'] = row[2]
                        data.append(bill)
                    return Response(data)
        except:
            print sys.exc_info()[0], sys.exc_info()[1]
            return Response("访问有误！")

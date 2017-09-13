#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:01
# @Author  : Neil.tang
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic import View
from django.contrib.auth.views import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from models import Menus
from django.utils.html import format_html
from django.db.models import Q
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponseForbidden

def make_menus_html(menus, parent_id=None, current_parent_id=None, active=None):
    """
    menus = Menus.objects.all()
    :param menus: 寻找的对象，传一个queryset对象
    :param parent_id: 父级菜单ID
    :param current_parent_id: 当前父级菜单ID
    :param active: 激活的菜单名
    :return:
    """
    make_html = ""
    for menu in menus:
        child_menu_flag = u"treeview"
        menu_right_flag = u'<span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span>'
        child_menu = u'<li><a href="{menu_url}"><i class="fa fa-circle-o"></i> {menu_name}</a></li>'
        child_menu_html = u'<ul class="treeview-menu">{make_child_menu_html}</ul>'
        master_menu_html = u"""
        <li class="{child_menu_flag} {active}">
            <a href="{menu_url}"><i class="fa {menu_icon}"></i> <span>{menu_name}</span>{menu_right_flag}</a>
            <ul class="treeview-menu">
            {children_menu_html}
            </ul>
        </li>"""
        children_menu_html = u"""
        <li class="treeview">
            <a href="{menu_url}"><i class="fa fa-circle-o"></i> <span>{menu_name}</span>{menu_right_flag}</a>
            {child_menu_html}
        </li>"""
        parent = menu.parent  # 获取当前菜单的父级菜单
        if current_parent_id == menu.id or (not parent and current_parent_id):
            continue  # 如果当前父级菜单ID是自己或没有父级菜单且有当前父级ID则跳过本次循环
        if not parent and current_parent_id is None:  # 如果没有父级菜单且当前父级ID是None
            make_children_menu_html = make_menus_html(menus, parent_id=parent_id, current_parent_id=menu.id)
            if not make_children_menu_html:
                menu_right_flag = ''
            menu_icon = "fa-eye"
            if hasattr(menu, 'icon_name'):
                menu_icon = menu.icon_name
            if menu.name == active:
                active_menu = 'active'
            else:
                active_menu = ''
            make_master_menu_html = master_menu_html.format(child_menu_flag=child_menu_flag,
                                                            active=active_menu,
                                                            menu_url=menu.url,
                                                            menu_icon=menu_icon,
                                                            menu_name=menu.name,
                                                            menu_right_flag=menu_right_flag,
                                                            children_menu_html=make_children_menu_html)
            make_html += make_master_menu_html
        elif parent and current_parent_id == parent.id:  # 如果有父级且当前父级ID是自己的父级ID
            make_child_menu_html = make_menus_html(menus, parent_id=current_parent_id, current_parent_id=menu.id)
            if make_child_menu_html:
                child_menu_html = child_menu_html.format(make_child_menu_html=make_child_menu_html)
                children_menu_html = children_menu_html.format(menu_url=menu.url,
                                                               menu_name=menu.name,
                                                               menu_right_flag=menu_right_flag,
                                                               child_menu_html=child_menu_html)
            else:
                children_menu_html = child_menu.format(menu_url=menu.url, menu_name=menu.name)
            make_html += children_menu_html
        else:
            continue
    return make_html


def make_menus_processor(request):
    UserPerms = request.user.get_all_permissions()
    menus_obj = Menus.objects.filter(Q(permission_id__in=UserPerms) | Q(permission_id=''))
    menus = make_menus_html(menus=menus_obj, active=u"监控")
    return format_html(menus)


def base(request):
    if isinstance(request.user, AnonymousUser):
        name = 'Guest'
        date_joined = None
    else:
        name = u"{first_name} {last_name}".format(first_name=request.user.first_name, last_name=request.user.last_name)
        date_joined = request.user.date_joined

    data = {
        "ROOT_MENU": make_menus_processor(request),
        "current_view_name": '',
        "site_name": '监控门户',
        "site_url": 'http://www.deppon.com',
        "current_user": {
            "nickname": name,
            "avatar_url": "/static/adminLTE/img/avatar5.png",
            "date_joined": date_joined,
        },
    }
    return data


class IndexView(View):
    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('Business.view_business'):
            return HttpResponseForbidden()

        return render(request, 'adminlte/index.html')


class LogoutView(View):
    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        django_logout(request)
        return redirect('/login/')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adminlte/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password, type=1)
        if not user:
            # or not user.is_staff
            message = '用户名或密码错误！'
            return render(request, 'adminlte/login.html', context={
                "message": message
            })
        django_login(request, user)
        return redirect('/')

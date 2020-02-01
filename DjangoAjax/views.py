import json
from datetime import datetime

from django.contrib.postgres import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from DjangoAjax.models import User

# 路由跳转到首页
from PublicMethod.common import model2json


def index(request):
    return render(request, "index.html", locals())


# 添加用户
def add(request):
    if request.method == "GET":
        return render(request, 'add.html', locals())
    res = {"code": "200", "err_msg": "", "data": ""};
    try:
        user_str = request.POST.get('user_str');
        user_json = json.loads(user_str);
        User.objects.create(user_no=user_json['user_no']
                            , name=user_json['name']
                            , age=user_json['age']
                            , password=user_json['password']
                            , create_date=datetime.now()
                            , modify_date=datetime.now());
    except Exception:
        res["code"] = "500";
        res["err_msg"] = '添加用户失败';
    return JsonResponse(res);


# 删除用户
def delItem(request, id):
    res = {"code": "200", "err_msg": "", "data": ""};
    try:
        item = User.objects.get(id=id);
        item.delete();
    except Exception:
        res["code"] = "500";
        res["err_msg"] = '删除用户失败';
    return JsonResponse(res);


# 修改用户
def edit(request, id):
    if request.method == "GET":
        return render(request, 'edit.html', locals());
    res = {"code": "200", "err_msg": "", "data": ""};
    try:
        item = User.objects.get(id=id);
        user_str = request.POST.get('user_str');
        user_json = json.loads(user_str);
        item.user_no = user_json['user_no'];
        item.name = user_json['name'];
        item.password = user_json['password'];
        item.age = user_json['age'];
        item.modify_date = datetime.now();
        item.save();
    except Exception:
        res["code"] = "500";
        res["err_msg"] = '修改用户失败';
    return JsonResponse(res);


# 根据主键获取对象
def getItem(request):
    if request.method == 'POST':
        res = {"code": "200", "err_msg": "", "data": ""};
        try:
            id = request.POST.get('id');
            item = User.objects.get(id=id);
            item_json = model2json(item);
            res['data'] = item_json;
        except Exception:
            res["code"] = "500";
            res["err_msg"] = '获取用户失败';
        return JsonResponse(res);


# 获取用户列表
def getList(request):
    if request.method == 'POST':
        res = {"code": "200", "err_msg": "", "data": ""};
        try:
            # 将字符串转化成对象
            search_str = request.POST.get('search_str');
            search_user = json.loads(search_str);
            # 根据查询条件查询
            userList = User.objects.filter(
                Q(user_no__contains=search_user["user_no"]) & Q(
                    name__contains=search_user["name"])).order_by('-modify_date').values();
            res["data"] = list(userList);
        except Exception:
            res["code"] = "500";
            res["err_msg"] = '获取用户失败';
        return JsonResponse(res);

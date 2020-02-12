import json
import uuid
from datetime import datetime

from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from DjangoAjax.models import User, Position, UserPosition, VALID, INVALID

# 路由跳转到首页
from PublicMethod.common import model2json


def index(request):
    return render(request, "index.html", locals())


# 添加用户
def add(request):
    if request.method == "GET":
        return render(request, 'add.html', locals())
    res = {"code": "200", "err_msg": "", "data": ""};
    user_str = request.POST.get('user_str');
    user_json = json.loads(user_str);
    # 显式的开启一个事务
    with transaction.atomic():
        # 创建事务保存点
        save_id = transaction.savepoint()
        try:
            # 添加人员
            user_id = uuid.uuid4();
            User.objects.create(
                id=user_id
                , user_no=user_json['user_no']
                , name=user_json['name']
                , age=user_json['age']
                , password=user_json['password']);
            # 添加人员岗位
            UserPosition.objects.create(
                user_id=user_id
                , position_id=user_json['pos_id']);
            # 提交订单成功，显式的提交一次事务
            transaction.savepoint_commit(save_id)
        except Exception as e:
            res["code"] = "500";
            res["err_msg"] = '添加用户失败';
            transaction.savepoint_rollback(save_id);
    return JsonResponse(res);


# 删除用户
def delItem(request, id):
    res = {"code": "200", "err_msg": "", "data": ""};
    try:
        item = User.objects.get(id=id);
        item.status = INVALID;
        item.save();
    except Exception as e:
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
    except Exception as e:
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
            # 获取岗位
            position_id = '';
            user_position_list = item.userposition_set;
            if user_position_list is not None:
                userposition = item.userposition_set.first();
                if userposition is not None:
                    position_id = userposition.position_id;
            item_json = model2json(item);
            item_json["pos_id"] = position_id;
            res['data'] = item_json;
        except Exception as e:
            res["code"] = "500";
            res["err_msg"] = '获取用户失败';
        return JsonResponse(res);


# 根据用户编码获取对象
def isUserNOExists(request):
    if request.method == 'POST':
        res = {"code": "200", "err_msg": "", "data": ""};
        try:
            user_no = request.POST.get('user_no');
            user_id = request.POST.get('user_id');
            item = '';
            if user_id == '':
                item = User.objects.filter(Q(status=VALID)
                                           & Q(user_no=user_no)).first();
            else:
                item = User.objects.filter(Q(status=VALID)
                                           & Q(user_no=user_no)
                                           & ~Q(id=user_id)).first();
            if item is not None:
                item_json = model2json(item);
                res['data'] = item_json;
        except Exception as e:
            res["code"] = "500";
            res["err_msg"] = '获取用户失败';
        return JsonResponse(res);


# 获取用户列表
def getList(request):
    if request.method == 'POST':
        res = {"code": "200", "err_msg": "", "data": "", "total": 0};
        try:
            # 将字符串转化成对象
            search_str = request.POST.get('search_str');
            search_user = json.loads(search_str);
            # 根据查询条件查询
            userList = User.objects.filter(
                Q(status=VALID)
                & Q(user_no__contains=search_user["user_no"])
                & Q(name__contains=search_user["name"])).order_by('-modify_date').values();
            currentPage = int(search_user["currentPage"]);
            itemsPerPage = int(search_user["itemsPerPage"]);
            startIndex = (currentPage - 1) * itemsPerPage;
            endIndex = currentPage * itemsPerPage;
            pageList = userList[startIndex:endIndex];
            res["data"] = list(pageList);
            res["total"] = userList.count();
        except Exception as e:
            res["code"] = "500";
            res["err_msg"] = '获取用户失败';
        return JsonResponse(res);


# 获取岗位列表
def getPositionList(request):
    res = {"code": "200", "err_msg": "", "data": ""};
    try:
        postionList = Position.objects.filter(status=VALID).order_by('pos_no').values();
        res["data"] = list(postionList);
    except Exception as e:
        res["code"] = "500";
        res["err_msg"] = '获取岗位失败';
    return JsonResponse(res);

import json
import sys

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from DjangoAjax.models import User


# 路由跳转到首页
def index(request):
    return render(request, "index.html", locals())


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
                Q(user_no__contains=search_user["user_no"]) & Q(name__contains=search_user["name"])).values();
            res["data"] = list(userList);
        except Exception:
            res["code"] = "500";
            res["err_msg"] = '获取用户失败';
        return JsonResponse(res);

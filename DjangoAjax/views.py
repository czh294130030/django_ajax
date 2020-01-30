import json

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
        userList = User.objects.all().values();
        res["data"] = list(userList)
        return JsonResponse(res);

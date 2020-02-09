"""django_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from DjangoAjax import views
from System import views as OrgView

urlpatterns = [
    # 用户
    url(r'^index/$', views.index, name="index"),  # 首页
    url(r'^add/$', views.add, name="add"),  # 添加
    url(r'^edit/(\d+)$', views.edit, name="edit"),  # 修改
    url(r'getList', views.getList),  # 获取列表
    url(r'getItem', views.getItem),  # 获取对象
    url(r'^delItem/(\d+)$', views.delItem),  # 删除对象

    # 组织
    url(r'^orgindex/$', OrgView.index, name="orgindex"),  # 首页
]

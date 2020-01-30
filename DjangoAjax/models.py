from django.db import models

class User(models.Model):
    UserNO=models.CharField('用户账户',max_length=200,default='');
    UserName=models.CharField('用户姓名',max_length=200,default='');
    Password=models.CharField('用户密码',max_length=200,default='');

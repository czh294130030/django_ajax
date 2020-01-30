from django.db import models


class User(models.Model):
    user_no = models.CharField('用户账户', max_length=200, default='')
    name = models.CharField('用户姓名', max_length=200, default='')
    age = models.IntegerField('用户年龄', default=0)
    password = models.CharField('用户密码', max_length=200, default='')

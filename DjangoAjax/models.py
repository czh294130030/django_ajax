from django.db import models


class User(models.Model):
    user_no = models.CharField('用户账户', max_length=200, null=True);
    name = models.CharField('用户姓名', max_length=200, null=True);
    age = models.IntegerField('用户年龄', null=True);
    password = models.CharField('用户密码', max_length=200, null=True);
    create_date = models.DateTimeField('创建时间', null=True);
    modify_date = models.DateTimeField('修改时间', null=True);

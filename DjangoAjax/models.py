import uuid
from datetime import datetime

from django.db import models

# 状态枚举
VALID = 1
INVALID = 0
STATUS = (
    (VALID, u'有效'),
    (INVALID, u'无效'),
)


# 基类，公共字段
class BaseClass(models.Model):
    # Django Model使用UUID作为主键
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    create_date = models.DateTimeField('创建时间', null=True);
    create_user = models.UUIDField('创建人', null=True);
    modify_date = models.DateTimeField('修改时间', null=True);
    modify_user = models.UUIDField('修改人', null=True);
    status = models.CharField('状态', max_length=1, choices=STATUS, default=VALID);

    class Meta:
        abstract = True;


# 用户
class User(BaseClass):
    user_no = models.CharField('用户账户', max_length=200, null=True);
    name = models.CharField('用户姓名', max_length=200, null=True);
    age = models.IntegerField('用户年龄', null=True);
    password = models.CharField('用户密码', max_length=200, null=True);

    class Meta:
        db_table = "sys_user";


# 岗位
class Position(BaseClass):
    pos_no = models.CharField('岗位编码', max_length=200, null=True);
    pos_name = models.CharField('岗位名称', max_length=200, null=True);

    class Meta:
        db_table = "sys_position";


# 人员岗位
class UserPosition(BaseClass):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True);
    position = models.ForeignKey('Position', on_delete=models.CASCADE, null=True);

    class Meta:
        db_table = "sys_userposition";

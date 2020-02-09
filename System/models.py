from django.db import models


# 通过命令创建ManageApp
# python manage.py startapp Manage
# 组织
class Organization(models.Model):
    org_no = models.CharField('组织编码', max_length=200, null=True);
    org_name = models.CharField('组织名称', max_length=200, null=True);
    create_date = models.DateTimeField('创建时间', null=True);
    modify_date = models.DateTimeField('修改时间', null=True);

    class Meta():
        # usr_organization为数据库表名
        db_table = 'usr_organization'

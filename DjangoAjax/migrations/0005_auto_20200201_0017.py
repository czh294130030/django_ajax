# Generated by Django 3.0.2 on 2020-01-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAjax', '0004_auto_20200130_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_date',
            field=models.DateField(null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='用户年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='用户姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, null=True, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_no',
            field=models.CharField(max_length=200, null=True, verbose_name='用户账户'),
        ),
    ]
# Generated by Django 3.0.2 on 2020-01-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAjax', '0002_auto_20200130_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='UserName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='UserNO',
            new_name='no',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name='用户年龄'),
        ),
    ]

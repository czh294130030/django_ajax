# Generated by Django 3.0.2 on 2020-02-10 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAjax', '0009_userpostion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postion',
            new_name='Position',
        ),
        migrations.RenameModel(
            old_name='UserPostion',
            new_name='UserPosition',
        ),
    ]

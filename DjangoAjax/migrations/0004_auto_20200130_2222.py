# Generated by Django 3.0.2 on 2020-01-30 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAjax', '0003_auto_20200130_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='no',
            new_name='user_no',
        ),
    ]
# Generated by Django 2.2.1 on 2019-07-10 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0004_delete_testdatabase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roadshape',
            old_name='road',
            new_name='block',
        ),
    ]

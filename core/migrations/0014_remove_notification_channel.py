# Generated by Django 3.1.6 on 2021-02-16 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210216_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='channel',
        ),
    ]

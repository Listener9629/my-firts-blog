# Generated by Django 2.2 on 2020-07-24 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_auto_20200709_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='published',
        ),
    ]

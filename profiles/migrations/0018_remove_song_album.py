# Generated by Django 2.1 on 2018-08-30 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20180830_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
    ]
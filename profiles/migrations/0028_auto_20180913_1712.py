# Generated by Django 2.1 on 2018-09-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20180907_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
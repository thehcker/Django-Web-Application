# Generated by Django 2.1 on 2018-08-29 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20180829_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default='foreign key', on_delete=django.db.models.deletion.CASCADE, to='profiles.Album'),
        ),
    ]

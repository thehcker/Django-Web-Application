# Generated by Django 2.1 on 2018-09-06 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_remove_songmodel_album'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SongModel',
            new_name='Song',
        ),
    ]

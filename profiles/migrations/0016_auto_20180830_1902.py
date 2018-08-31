# Generated by Django 2.1 on 2018-08-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20180830_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='albums',
            field=models.IntegerField(default='mylocationdefault', max_length=20),
        ),
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.ForeignKey(default='mylocationdefault', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='profiles.Album'),
        ),
    ]

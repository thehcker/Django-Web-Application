# Generated by Django 2.1 on 2018-08-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20180809_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=120)),
                ('albums', models.TextField(max_length=120)),
                ('genre', models.TextField(default='mylocationdefault', max_length=100)),
                ('songs', models.TextField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('genre', models.TextField(max_length=120)),
                ('producer', models.TextField(default='mylocationdefault', max_length=100)),
            ],
        ),
    ]

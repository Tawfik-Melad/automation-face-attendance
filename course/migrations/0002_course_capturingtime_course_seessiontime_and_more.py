# Generated by Django 4.2.1 on 2023-05-12 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='capturingTime',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='course',
            name='seessionTime',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='course',
            name='sessionDay',
            field=models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default='Sunday', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='sessionHour',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='course',
            name='sessionPlace',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='totalNumberOfLectures',
            field=models.IntegerField(default=13),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('lecture', 'lecture'), ('section', 'section')], default='lecture', max_length=10),
        ),
    ]

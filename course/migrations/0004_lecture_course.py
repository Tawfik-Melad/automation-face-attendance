# Generated by Django 4.2.1 on 2023-05-15 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='course.course'),
        ),
    ]

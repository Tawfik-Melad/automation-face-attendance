# Generated by Django 4.1.6 on 2023-05-24 11:38

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_image_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='.jpg', upload_to=users.models.profile_image_upload_to),
        ),
    ]

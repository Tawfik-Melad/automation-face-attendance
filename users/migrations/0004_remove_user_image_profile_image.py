# Generated by Django 4.2.1 on 2023-05-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_image_user_image_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='.jpg', upload_to='profile_pics'),
        ),
    ]

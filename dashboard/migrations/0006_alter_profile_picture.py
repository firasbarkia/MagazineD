# Generated by Django 4.1.7 on 2023-03-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='user.png', upload_to='profile_images'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='Magazine/Athena/Athena/static/images/user.png', upload_to='profile_images'),
        ),
    ]

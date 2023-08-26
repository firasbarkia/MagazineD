# Generated by Django 4.1.7 on 2023-03-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_alter_article_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='etat',
            field=models.CharField(choices=[('accepted', 'accepted'), ('refused', 'refused'), ('panding', 'panding')], default='panding', max_length=20),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-30 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produit', '0002_alter_productseries_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productseries',
            options={'verbose_name_plural': 'Series'},
        ),
    ]

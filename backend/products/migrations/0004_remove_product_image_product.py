# Generated by Django 4.2.4 on 2024-04-08 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_creator_remove_product_modifier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_product',
        ),
    ]

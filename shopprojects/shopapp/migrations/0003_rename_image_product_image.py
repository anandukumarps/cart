# Generated by Django 4.0.6 on 2022-07-14 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_rename_slug_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]
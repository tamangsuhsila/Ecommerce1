# Generated by Django 5.0.6 on 2024-06-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=1000),
        ),
    ]

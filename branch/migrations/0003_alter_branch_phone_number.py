# Generated by Django 5.0.6 on 2024-06-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_alter_branch_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-12 08:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='static/blog')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_to', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['publish'],
            },
        ),
    ]

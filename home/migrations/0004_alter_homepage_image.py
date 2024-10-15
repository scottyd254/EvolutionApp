# Generated by Django 5.0.9 on 2024-10-13 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_image'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only, 16:9 ratio recommended at least 1024 x 768 px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-26 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_images_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='file_path',
        ),
    ]

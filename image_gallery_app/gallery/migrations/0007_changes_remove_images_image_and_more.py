# Generated by Django 5.0.6 on 2024-07-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_images_file_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=256, null=True)),
                ('change_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='upload_time',
        ),
    ]

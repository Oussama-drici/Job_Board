# Generated by Django 4.1 on 2022-08-13 13:29

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='published_at',
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.upload_img),
        ),
    ]

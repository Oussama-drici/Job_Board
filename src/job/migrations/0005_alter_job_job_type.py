# Generated by Django 4.1 on 2022-08-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], max_length=15),
        ),
    ]

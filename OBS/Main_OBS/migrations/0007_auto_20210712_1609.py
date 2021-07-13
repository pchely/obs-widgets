# Generated by Django 3.2.4 on 2021-07-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_OBS', '0006_auto_20210708_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obs_model',
            name='slug',
        ),
        migrations.AlterField(
            model_name='obs_model',
            name='name',
            field=models.SlugField(unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='obs_model',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
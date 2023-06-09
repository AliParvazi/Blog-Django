# Generated by Django 4.2 on 2023-04-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.TimeField(default='16:04:11'),
        ),
    ]

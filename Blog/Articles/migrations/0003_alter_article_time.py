# Generated by Django 4.2 on 2023-04-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_alter_article_image_alter_article_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.TimeField(default='16:52:36'),
        ),
    ]

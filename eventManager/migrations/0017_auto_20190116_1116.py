# Generated by Django 2.1.4 on 2019-01-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0016_auto_20190114_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='url',
            field=models.ImageField(upload_to='imgs'),
        ),
    ]
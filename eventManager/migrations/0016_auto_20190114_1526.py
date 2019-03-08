# Generated by Django 2.1.4 on 2019-01-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0015_auto_20190114_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='site',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

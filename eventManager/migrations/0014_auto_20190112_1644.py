# Generated by Django 2.1.4 on 2019-01-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0013_auto_20190112_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='services',
            field=models.ManyToManyField(related_name='eventFk', to='eventManager.Service'),
        ),
    ]
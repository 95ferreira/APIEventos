# Generated by Django 2.1.4 on 2019-02-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0024_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='vpmf/static/imgs'),
        ),
    ]

# Generated by Django 2.1.4 on 2019-01-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0020_auto_20190116_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='static/imgs'),
        ),
    ]

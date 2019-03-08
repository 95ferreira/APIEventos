# Generated by Django 2.1.4 on 2018-12-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guests',
            name='contactFk',
        ),
        migrations.RemoveField(
            model_name='service',
            name='contactFk',
        ),
        migrations.AddField(
            model_name='guests',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guests',
            name='tel',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='tel',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
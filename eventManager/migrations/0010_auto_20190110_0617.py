# Generated by Django 2.1.4 on 2019-01-10 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0009_event_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteImages',
            new_name='Images',
        ),
        migrations.RenameModel(
            old_name='EventProg',
            new_name='Prog',
        ),
    ]

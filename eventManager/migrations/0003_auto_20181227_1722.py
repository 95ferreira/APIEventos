# Generated by Django 2.1.4 on 2018-12-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0002_auto_20181224_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventprog',
            name='eventFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prog', to='eventManager.Event'),
        ),
    ]

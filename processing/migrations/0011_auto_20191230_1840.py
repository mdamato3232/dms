# Generated by Django 2.2.6 on 2019-12-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0010_auto_20191230_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmissions',
            name='time_offset',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transmissions',
            name='time_slot',
            field=models.SmallIntegerField(null=True),
        ),
    ]
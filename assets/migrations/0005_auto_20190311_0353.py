# Generated by Django 2.1.7 on 2019-03-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20190305_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='file_main',
            new_name='file_1',
        ),
        migrations.AddField(
            model_name='asset',
            name='file_4',
            field=models.FileField(blank=True, upload_to='files/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='file_5',
            field=models.FileField(blank=True, upload_to='files/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='file_6',
            field=models.FileField(blank=True, upload_to='files/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d'),
        ),
    ]

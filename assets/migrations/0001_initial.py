# Generated by Django 2.1.7 on 2019-03-03 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnumber', models.CharField(max_length=200)),
                ('serialnumber', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('acquire_date', models.DateField(blank=True)),
                ('cost', models.IntegerField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('website', models.URLField(blank=True)),
                ('configuration', models.FileField(blank=True, upload_to='files/%y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['sector'],
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='cbp_component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assets.Components'),
        ),
        migrations.AddField(
            model_name='asset',
            name='cbp_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assets.Sectors'),
        ),
    ]
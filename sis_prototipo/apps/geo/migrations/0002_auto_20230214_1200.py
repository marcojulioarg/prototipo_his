# Generated by Django 3.2.16 on 2023-02-14 18:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='pobfem',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población femenina'),
        ),
        migrations.AddField(
            model_name='entidad',
            name='pobmas',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población masculina'),
        ),
        migrations.AddField(
            model_name='entidad',
            name='pobtot',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población total'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='pobfem',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población femenina'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='pobmas',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población masculina'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='pobtot',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población total'),
        ),
        migrations.AddField(
            model_name='manzana',
            name='pobfem',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población femenina'),
        ),
        migrations.AddField(
            model_name='manzana',
            name='pobmas',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población masculina'),
        ),
        migrations.AddField(
            model_name='manzana',
            name='pobtot',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población total'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='pobfem',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población femenina'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='pobmas',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población masculina'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='pobtot',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Población total'),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='manzana',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.DeleteModel(
            name='Demograficos',
        ),
    ]

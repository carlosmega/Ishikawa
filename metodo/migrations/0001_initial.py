# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCausa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causa', models.CharField(blank=True, max_length=350, null=True)),
                ('sev', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('det', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('occ', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('rpn', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('solucion', models.CharField(blank=True, max_length=350, null=True)),
                ('responsable', models.CharField(blank=True, max_length=350, null=True)),
                ('fecha_cierre', models.DateField(blank=True, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelHallazgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallazgo', models.CharField(max_length=150)),
                ('creado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='modelcausa',
            name='hallazgo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metodo.ModelHallazgo'),
        ),
    ]

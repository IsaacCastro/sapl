# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0028_auto_20160419_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoria',
            name='primeiro_autor',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Primeiro Autor'),
        ),
    ]

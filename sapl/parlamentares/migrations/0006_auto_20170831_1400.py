# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-31 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0005_auto_20170814_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='votante',
            options={'permissions': (('can_vote', 'Can Vote'),), 'verbose_name': 'Usuário Votante', 'verbose_name_plural': 'Usuários Votantes'},
        ),
    ]
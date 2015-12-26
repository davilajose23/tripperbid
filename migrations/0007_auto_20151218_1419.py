# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20151218_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='subasta',
            name='pago',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 14, 19, 57, 741488), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 14, 19, 57, 739605), verbose_name=b'date payed'),
        ),
    ]

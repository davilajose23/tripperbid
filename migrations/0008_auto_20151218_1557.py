# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20151218_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 15, 57, 7, 518012), verbose_name=b'date payed'),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 15, 57, 7, 526880), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 15, 57, 7, 525777), verbose_name=b'date payed'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20151218_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='piramide',
            name='limite',
            field=models.IntegerField(default=14),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 13, 48, 12, 893145), verbose_name=b'date payed'),
        ),
    ]

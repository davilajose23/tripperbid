# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_auto_20151218_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='ganador',
            name='cobrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 16, 31, 8, 993363), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 16, 31, 8, 988174), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 16, 31, 8, 992339), verbose_name=b'date payed'),
        ),
    ]

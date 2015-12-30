# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0018_auto_20151228_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='gender',
            field=models.CharField(default=b'O', max_length=1, choices=[(b'F', b'female'), (b'M', b'male'), (b'O', b'other')]),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 2, 51, 28, 515329), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 2, 51, 28, 507777), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 2, 51, 28, 513552), verbose_name=b'date payed'),
        ),
    ]

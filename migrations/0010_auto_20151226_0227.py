# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_auto_20151218_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='model_pic',
            field=models.ImageField(default=b'pictures/foto.jpg', upload_to=b'pictures/'),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 27, 36, 381987), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 27, 36, 375930), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 27, 36, 380606), verbose_name=b'date payed'),
        ),
    ]

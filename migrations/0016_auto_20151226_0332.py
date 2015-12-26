# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0015_auto_20151226_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 3, 32, 34, 792510), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 3, 32, 34, 787593), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='model_pic',
            field=models.ImageField(default=b'photos/foto.jpg', upload_to=b'photos/'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 3, 32, 34, 791336), verbose_name=b'date payed'),
        ),
    ]

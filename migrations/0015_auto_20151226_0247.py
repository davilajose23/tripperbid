# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0014_auto_20151226_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 47, 52, 822812), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 47, 52, 818015), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='model_pic',
            field=models.ImageField(default=b'media/photos/foto.jpg', upload_to=b'media/photos/'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 47, 52, 821704), verbose_name=b'date payed'),
        ),
    ]

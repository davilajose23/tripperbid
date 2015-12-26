# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_auto_20151226_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 44, 44, 230060), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 44, 44, 223631), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='model_pic',
            field=models.ImageField(default=b'', upload_to=b'media/photos'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 44, 44, 228682), verbose_name=b'date payed'),
        ),
    ]

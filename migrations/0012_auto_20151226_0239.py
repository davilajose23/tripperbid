# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_auto_20151226_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 39, 7, 18796), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 39, 7, 13798), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='model_pic',
            field=models.ImageField(default=b'', upload_to=django.core.files.storage.FileSystemStorage(location=b'/media/photos')),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 2, 39, 7, 17685), verbose_name=b'date payed'),
        ),
    ]

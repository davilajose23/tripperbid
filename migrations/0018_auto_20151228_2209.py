# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import trips.utils
import datetime
import trips.models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0017_auto_20151226_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='subasta',
            name='recaudado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 28, 22, 9, 46, 367103), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 28, 22, 9, 46, 362623), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pp',
            field=models.ImageField(default=b'photos/foto.jpg', storage=trips.utils.OverwriteStorage(), upload_to=trips.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 28, 22, 9, 46, 366220), verbose_name=b'date payed'),
        ),
    ]

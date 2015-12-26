# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import trips.models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0016_auto_20151226_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='model_pic',
        ),
        migrations.AddField(
            model_name='usuario',
            name='pp',
            field=models.ImageField(default=b'photos/foto.jpg', upload_to=trips.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='ganador',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 3, 38, 42, 211628), verbose_name=b'date win'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 3, 38, 42, 200675), verbose_name=b'register date'),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 26, 3, 38, 42, 205694), verbose_name=b'date payed'),
        ),
    ]

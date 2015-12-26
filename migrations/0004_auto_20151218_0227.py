# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20151218_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 2, 27, 10, 893927), verbose_name=b'date payed'),
        ),
    ]

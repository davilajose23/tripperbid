# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20151218_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ganador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 12, 18, 14, 16, 26, 899215), verbose_name=b'date win')),
                ('subasta', models.ForeignKey(to='trips.Subasta')),
                ('usuario', models.ForeignKey(to='trips.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='piramide',
            name='limite',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 14, 16, 26, 898322), verbose_name=b'date payed'),
        ),
    ]

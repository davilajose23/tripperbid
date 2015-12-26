# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followed', models.ForeignKey(related_name='followed_user', to='trips.Usuario')),
                ('follower', models.ForeignKey(related_name='follower_user', to='trips.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 1, 49, 8, 855413), verbose_name=b'date payed'),
        ),
    ]

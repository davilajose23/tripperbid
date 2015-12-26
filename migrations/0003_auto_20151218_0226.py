# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20151218_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followed', models.ForeignKey(related_name='followed_user', to='trips.Usuario')),
                ('follower', models.ForeignKey(related_name='follower_user', to='trips.Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.AlterField(
            model_name='usuariopiramide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 2, 26, 41, 893838), verbose_name=b'date payed'),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]

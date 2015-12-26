# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Piramide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished', models.BooleanField(default=False)),
                ('inscritos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default=b'example@example.com', unique=True, max_length=254)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPiramide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lider', models.BooleanField(default=False)),
                ('nivel', models.IntegerField(default=1)),
                ('finished', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 12, 17, 17, 4, 44, 362389), verbose_name=b'date payed')),
                ('piramide', models.ForeignKey(to='trips.Piramide')),
                ('usuario', models.ForeignKey(to='trips.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='piramide',
            name='subasta',
            field=models.ForeignKey(to='trips.Subasta'),
        ),
    ]

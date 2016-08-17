# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autobus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regnum', models.CharField(max_length=b'6', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80')),
            ],
            options={
                'verbose_name': '\u0410\u0432\u0442\u043e\u0431\u0443\u0441',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u0431\u0443\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(blank=True)),
                ('counter', models.IntegerField(default=b'0', null=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longtitude', models.FloatField(null=True, blank=True)),
                ('duration', models.DurationField(default=b'0', null=True)),
                ('kilometrage', models.FloatField(default=b'0', null=True)),
                ('bus', models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd0\xb1\xd1\x83\xd1\x81', to='Counter.autobus')),
            ],
            options={
                'verbose_name': '\u0421\u0447\u0435\u0442\u0447\u0438\u043a',
                'verbose_name_plural': '\u0421\u0447\u0435\u0442\u0447\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=20, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('lastname', models.CharField(max_length=20, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('bus', models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd0\xb1\xd1\x83\xd1\x81', to='Counter.autobus')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u0438',
            },
        ),
    ]

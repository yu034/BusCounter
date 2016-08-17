# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='hhkilometrage',
            field=models.FloatField(default=b'0', null=True),
        ),
    ]

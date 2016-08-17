# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counter', '0002_counter_hhkilometrage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='hhkilometrage',
        ),
    ]

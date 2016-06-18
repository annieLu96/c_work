# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20160312_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='comment',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfs', '0003_auto_20161108_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Rated',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]

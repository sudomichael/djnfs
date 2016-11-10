# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfs', '0005_auto_20161108_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='average',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='kind',
            field=models.TextField(null=True),
        ),
    ]

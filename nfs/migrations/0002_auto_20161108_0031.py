# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='poster',
            new_name='Poster',
        ),
        migrations.AddField(
            model_name='movie',
            name='Error',
            field=models.TextField(default='NoError'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='Response',
            field=models.TextField(default='NoResponse'),
            preserve_default=False,
        ),
    ]

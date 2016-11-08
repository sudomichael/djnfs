# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfs', '0004_movie_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Awards',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='BoxOffice',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='DVD',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Error',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Language',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Metascore',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Plot',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Poster',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Production',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Rated',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Response',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Website',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Writer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbID',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbRating',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbVotes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoConsensus',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoFresh',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoImage',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoMeter',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoRating',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoReviews',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoRotten',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoURL',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoUserMeter',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoUserRating',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tomatoUserReviews',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='totalSeasons',
            field=models.TextField(null=True),
        ),
    ]

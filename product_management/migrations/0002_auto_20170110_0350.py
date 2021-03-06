# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='category',
            name='Updated',
            field=models.DateField(null=True, blank=True),
        ),
    ]

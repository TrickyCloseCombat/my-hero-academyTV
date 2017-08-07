# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='videolink',
            field=models.TextField(default=datetime.datetime(2017, 8, 7, 22, 57, 59, 953902, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

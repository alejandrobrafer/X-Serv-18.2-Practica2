# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20180403_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='name',
        ),
        migrations.AddField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=200, default=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0003_auto_20180403_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='num',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='URL',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='url',
            name='num',
            field=models.IntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150810_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='credentials',
            new_name='credential',
        ),
    ]

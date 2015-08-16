# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150810_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='user',
            new_name='credentials',
        ),
    ]

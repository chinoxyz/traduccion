# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150810_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='validated_email',
            field=models.BooleanField(default=False),
        ),
    ]

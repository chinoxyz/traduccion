# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='company',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='initial_email',
        ),
        migrations.AddField(
            model_name='appuser',
            name='email',
            field=models.EmailField(default='', unique=True, max_length=254),
            preserve_default=False,
        ),
    ]

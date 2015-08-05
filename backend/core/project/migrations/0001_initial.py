# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('language', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('estimated_price', models.FloatField(null=True, blank=True)),
                ('status', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('details', models.TextField()),
                ('conditions', models.TextField()),
                ('information', models.TextField()),
                ('expected_deadline', models.DateTimeField()),
                ('specifications', models.TextField(blank=True)),
                ('adaptations', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAsignation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('worker_price', models.FloatField(null=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(null=True, blank=True)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TraductionProject',
            fields=[
                ('project_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='project.Project')),
                ('text', models.TextField(null=True, blank=True)),
                ('textURL', models.CharField(max_length=256, null=True, blank=True)),
                ('number_of_words', models.IntegerField(null=True, blank=True)),
                ('number_of_pages', models.IntegerField(null=True, blank=True)),
                ('destination_language', models.ForeignKey(related_name='destiny', to='language.Language')),
                ('origin_language', models.ForeignKey(related_name='origin', to='language.Language')),
            ],
            bases=('project.project',),
        ),
        migrations.AddField(
            model_name='projectasignation',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
        migrations.AddField(
            model_name='projectasignation',
            name='worker',
            field=models.ForeignKey(to='user.AppUser'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(to='user.AppUser'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('img', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=300)),
                ('caption', models.TextField()),
                ('button_link', models.URLField(null=True, default='register')),
                ('button_title', models.CharField(max_length=20, default='View details')),
            ],
        ),
        migrations.CreateModel(
            name='StatusReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to='payments.User')),
            ],
        ),
    ]

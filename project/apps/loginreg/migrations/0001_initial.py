# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('damage', models.IntegerField()),
                ('users', models.ManyToManyField(to='loginreg.User')),
            ],
            options={
                'db_table': 'weapons',
            },
        ),
    ]

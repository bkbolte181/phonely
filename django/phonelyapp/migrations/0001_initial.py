# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('phone_number', models.CharField(max_length=15, unique=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('interests', models.TextField()),
                ('rating', models.IntegerField()),
                ('safe_mode', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('person_one', models.ForeignKey(related_name=b'convo_person_one', primary_key=True, serialize=False, to='phonelyapp.Person')),
                ('person_two', models.ForeignKey(related_name=b'convo_person_two', to='phonelyapp.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

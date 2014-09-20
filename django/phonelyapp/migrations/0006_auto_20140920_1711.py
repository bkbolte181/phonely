# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonelyapp', '0005_person_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='person_one',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='person_two',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.RemoveField(
            model_name='person',
            name='status',
        ),
        migrations.AddField(
            model_name='person',
            name='partner',
            field=models.ForeignKey(blank=True, to='phonelyapp.Person', null=True),
            preserve_default=True,
        ),
    ]

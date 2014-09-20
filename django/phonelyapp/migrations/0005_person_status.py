# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonelyapp', '0004_auto_20140920_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(default='idle', max_length=30),
            preserve_default=False,
        ),
    ]

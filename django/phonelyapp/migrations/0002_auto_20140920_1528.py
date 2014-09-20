# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonelyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='safe_mode',
            field=models.BooleanField(default=True),
        ),
    ]

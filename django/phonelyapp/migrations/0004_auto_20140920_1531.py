# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonelyapp', '0003_auto_20140920_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]

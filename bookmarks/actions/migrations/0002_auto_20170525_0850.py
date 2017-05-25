# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, related_name='target_obj', to='contenttypes.ContentType'),
        ),
    ]

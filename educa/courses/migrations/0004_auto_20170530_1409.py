# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170529_0536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='cource',
            new_name='course',
        ),
    ]

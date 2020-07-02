# Generated by Django 3.0.7 on 2020-07-01 18:17

import build_health.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autocomplete', '0003_remove_autocompleterecord_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='autocompleterecord',
            name='created_at',
            field=build_health.models.UnixTimestampField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='autocompleterecord',
            name='updated_at',
            field=build_health.models.UnixTimestampField(auto_created=True, null=True),
        ),
    ]

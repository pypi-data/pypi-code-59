# Generated by Django 2.2.7 on 2019-11-18 12:45

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191117_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_types',
            name='props',
            field=bitfield.models.BitField((('isEvent', 'Является событием'), ('compulsory_reading', 'Обязательное прочтение')), db_index=True, default=0),
        ),
    ]

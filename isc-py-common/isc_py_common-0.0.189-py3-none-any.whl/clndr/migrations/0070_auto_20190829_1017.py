# Generated by Django 2.2.4 on 2019-08-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clndr', '0069_auto_20190829_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift_day_relax',
            name='relaxorder',
            field=models.PositiveIntegerField(),
        ),
    ]

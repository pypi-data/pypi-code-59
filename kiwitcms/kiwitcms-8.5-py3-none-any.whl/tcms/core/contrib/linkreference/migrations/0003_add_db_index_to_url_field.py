# Generated by Django 2.2.5 on 2019-09-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkreference', '0002_update_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkreference',
            name='url',
            field=models.URLField(db_index=True),
        ),
    ]

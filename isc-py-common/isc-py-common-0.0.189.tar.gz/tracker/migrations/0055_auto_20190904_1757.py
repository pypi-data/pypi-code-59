# Generated by Django 2.2.5 on 2019-09-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0054_auto_20190904_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='checksum',
            field=models.CharField(max_length=255),
        ),
    ]

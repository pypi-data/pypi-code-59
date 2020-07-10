# Generated by Django 2.2 on 2019-04-14 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('isc_common', '0020_auto_20190414_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='params',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='user_permission',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='usergroup_permission',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='widgets_trees',
            name='lastmodified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
    ]

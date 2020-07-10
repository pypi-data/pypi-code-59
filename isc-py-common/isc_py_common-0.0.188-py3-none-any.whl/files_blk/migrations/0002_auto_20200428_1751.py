# Generated by Django 2.2.12 on 2020-04-28 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('files_blk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления'),
        ),
        migrations.AddField(
            model_name='files',
            name='deliting',
            field=models.BooleanField(default=True, verbose_name='Возможность удаления'),
        ),
        migrations.AddField(
            model_name='files',
            name='editing',
            field=models.BooleanField(default=True, verbose_name='Возможность редактирования'),
        ),
        migrations.AddField(
            model_name='files',
            name='lastmodified',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AddField(
            model_name='files_group',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата мягкого удаления'),
        ),
        migrations.AddField(
            model_name='files_group',
            name='deliting',
            field=models.BooleanField(default=True, verbose_name='Возможность удаления'),
        ),
        migrations.AddField(
            model_name='files_group',
            name='editing',
            field=models.BooleanField(default=True, verbose_name='Возможность редактирования'),
        ),
        migrations.AddField(
            model_name='files_group',
            name='lastmodified',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='files',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='files_group',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
    ]

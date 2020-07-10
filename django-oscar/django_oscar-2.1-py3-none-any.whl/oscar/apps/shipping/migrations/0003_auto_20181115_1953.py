# Generated by Django 2.0.7 on 2018-11-15 19:53

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20150604_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderanditemcharges',
            name='name',
            field=models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='weightband',
            name='upper_limit',
            field=models.DecimalField(db_index=True, decimal_places=3, help_text='Enter upper limit of this weight band in kg. The lower limit will be determined by the other weight bands.', max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Upper Limit'),
        ),
        migrations.AlterField(
            model_name='weightbased',
            name='name',
            field=models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Name'),
        ),
    ]

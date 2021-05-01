# Generated by Django 2.0.13 on 2020-12-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20201221_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_excl_tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Order total (excl. tax)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='total_incl_tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Order total (inc. tax)'),
            preserve_default=False,
        ),
    ]

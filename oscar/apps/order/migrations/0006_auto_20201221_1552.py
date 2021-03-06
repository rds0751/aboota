# Generated by Django 2.0.13 on 2020-12-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_update_email_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_excl_tax',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Order total (excl. tax)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_incl_tax',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Order total (inc. tax)'),
        ),
    ]

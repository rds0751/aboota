# Generated by Django 2.2.3 on 2021-02-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_auto_20150604_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automaticproductlist',
            name='method',
            field=models.CharField(choices=[('Bestselling', 'Bestselling products'), ('RecentlyAdded', 'Recently added products'), ('JRIndia', 'JR Products')], max_length=128, verbose_name='Method'),
        ),
    ]

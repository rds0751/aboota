# Generated by Django 2.2.13 on 2021-04-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_auto_20210428_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gst',
            field=models.FloatField(null=True, verbose_name='GST'),
        ),
    ]

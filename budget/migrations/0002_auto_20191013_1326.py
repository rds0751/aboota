# Generated by Django 2.1.7 on 2019-10-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenseinfo',
            old_name='users',
            new_name='user_expense',
        ),
    ]

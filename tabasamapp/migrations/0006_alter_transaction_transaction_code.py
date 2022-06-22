# Generated by Django 4.0.5 on 2022-06-22 20:56

from django.db import migrations, models
import tabasamapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tabasamapp', '0005_alter_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_code',
            field=models.CharField(default=tabasamapp.models.code_gen, max_length=254, unique=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabasamapp', '0010_useraccount_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='info',
            field=models.TextField(default='E Tabasamu cares for your financial needs', null=True),
        ),
    ]

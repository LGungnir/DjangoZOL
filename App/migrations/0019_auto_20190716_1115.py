# Generated by Django 2.2.3 on 2019-07-16 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_floor_floorgood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorgood',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

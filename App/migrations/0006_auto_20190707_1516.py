# Generated by Django 2.2.3 on 2019-07-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20190707_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='ram',
            field=models.CharField(default='8', max_length=32),
        ),
        migrations.AlterField(
            model_name='good',
            name='rom',
            field=models.CharField(default='128', max_length=32),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_auto_20190716_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floorgood',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='floorgood',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_auto_20190714_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='receive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.Receive'),
        ),
    ]

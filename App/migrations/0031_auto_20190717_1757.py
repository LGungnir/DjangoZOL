# Generated by Django 2.2.3 on 2019-07-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0030_grandtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='grandtype',
            name='ancestral',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.AncestralType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parenttype',
            name='grand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.GrandType'),
            preserve_default=False,
        ),
    ]

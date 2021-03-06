# Generated by Django 2.2.3 on 2019-07-06 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=32)),
                ('ename', models.CharField(max_length=32)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('money', models.FloatField(default=0.0, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField(default=1)),
                ('feature', models.CharField(max_length=128)),
                ('network', models.CharField(max_length=32)),
                ('color', models.CharField(default='黑色', max_length=32)),
                ('ram', models.IntegerField(default=4)),
                ('rom', models.IntegerField(default=16)),
                ('img', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Brand')),
            ],
        ),
    ]

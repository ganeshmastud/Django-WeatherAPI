# Generated by Django 3.0.7 on 2020-06-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=40)),
                ('temperature', models.FloatField(default=False)),
                ('feels_like', models.FloatField(default=False)),
                ('min_temp', models.FloatField(default=False)),
                ('max_temp', models.FloatField(default=False)),
                ('description', models.CharField(default=False, max_length=40)),
                ('icon', models.CharField(default=False, max_length=40)),
            ],
        ),
    ]

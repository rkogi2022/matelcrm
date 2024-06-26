# Generated by Django 5.0.1 on 2024-04-16 05:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=50)),
                ('houserent', models.PositiveIntegerField(default=0)),
                ('homeinternet', models.PositiveIntegerField(default=0)),
                ('monthlyfuel', models.PositiveIntegerField(default=0)),
                ('carmaintenance', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('totalcost', models.PositiveIntegerField(default='0')),
            ],
        ),
    ]

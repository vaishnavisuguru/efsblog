# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-19 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFunds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('beginning_assets', models.CharField(max_length=200)),
                ('ending_assets', models.CharField(max_length=200)),
                ('net_flow', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutualfunds', to='portfolio.Customer')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('linkedInId', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter_link', models.URLField(blank=True, max_length=300)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('website', models.URLField(blank=True, max_length=300)),
                ('show_on_site', models.BooleanField(default=True)),
                ('founded_on_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funding_date', models.DateTimeField(blank=True, null=True)),
                ('funding_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stages', models.CharField(blank=True, choices=[('Series A', 'Series A'), ('Series B', 'Series B'), ('Series C', 'Series C'), ('Series D', 'Series D'), ('Series E', 'Series E'), ('Series F', 'Series F')], max_length=50, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='company.Company')),
                ('investor_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor_company', to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='market',
            field=models.ManyToManyField(blank=True, null=True, to='company.Market'),
        ),
    ]

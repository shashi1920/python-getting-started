# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tables',
            fields=[
                #('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                #('when', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True)),
                ('url', models.CharField(max_length=1001, blank=True, null=True)),
                ('url_2', models.CharField(max_length=1001, blank=True, null=True)),
                ('link_to_solicitation', models.CharField(max_length=1001, blank=True, null=True)),
                ('agency', models.CharField(max_length=1001, blank=True, null=True)),
                ('fsg', models.CharField(max_length=1001, blank=True, null=True)),
                ('fsg_description', models.CharField(max_length=1001, blank=True, null=True)),
                ('psc_code', models.CharField(max_length=1001, blank=True, null=True)),
                ('PSC_description', models.CharField(max_length=1001, blank=True, null=True)),
                ('source', models.CharField(max_length=1001, blank=True, null=True)),
                ('title', models.CharField(max_length=1001, blank=True, null=True)),
                ('keywords', models.CharField(max_length=1001, blank=True, null=True)),
                ('email', models.CharField(max_length=1001, blank=True, null=True)),
                ('phone', models.CharField(max_length=1001, blank=True, null=True)),
                ('contract_specialist', models.CharField(max_length=1001, blank=True, null=True)),
                ('contract_officer', models.CharField(max_length=1001, blank=True, null=True)),
                ('set_aside', models.CharField(max_length=1001, blank=True, null=True)),
                ('naics_code', models.IntegerField(max_length=1001, blank=True, null=True)),
                ('contact_info', models.CharField(max_length=1001, blank=True, null=True)),
                ('place_of_performance', models.CharField(max_length=1001, blank=True, null=True)),
                ('description', models.CharField(max_length=1001, blank=True, null=True)),
                ('Solicitation_Number', models.CharField(max_length=1001, blank=True, null=True)),
                ('Notice_Type', models.CharField(max_length=1001, blank=True, null=True)),
                ('Point_of_Contact', models.CharField(max_length=1001, blank=True, null=True)),
                ('Point_of_Contact_email', models.CharField(max_length=1001, blank=True, null=True)),

            ],
        ),
    ]

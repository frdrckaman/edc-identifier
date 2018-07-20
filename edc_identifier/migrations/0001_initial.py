# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields
import django_revision.revision_field
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
import edc_model_fields.fields.uuid_auto_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdentifierHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=25, unique=True)),
                ('identifier_type', models.CharField(max_length=25)),
                ('identifier_prefix', models.CharField(max_length=25, null=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='IdentifierTracker',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_model_fields.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_model_fields.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_model_fields.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_model_fields.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('identifier', models.CharField(db_index=True, max_length=25)),
                ('identifier_string', models.CharField(db_index=True, max_length=50)),
                ('root_number', models.IntegerField(db_index=True)),
                ('counter', models.IntegerField(db_index=True)),
                ('identifier_type', models.CharField(max_length=35)),
                ('device_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'ordering': ['root_number', 'counter'],
            },
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_model_fields.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_model_fields.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_model_fields.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_id', models.IntegerField(default=99)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubjectIdentifier',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_model_fields.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_model_fields.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_model_fields.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_model_fields.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('identifier', models.CharField(editable=False, max_length=36, unique=True)),
                ('padding', models.IntegerField(default=4, editable=False)),
                ('sequence_number', models.IntegerField()),
                ('device_id', models.IntegerField(default=0)),
                ('is_derived', models.BooleanField(default=False)),
                ('sequence_app_label', models.CharField(default='identifier', editable=False, max_length=50)),
                ('sequence_model_name', models.CharField(default='sequence', editable=False, max_length=50)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='identifiertracker',
            unique_together=set([('root_number', 'counter')]),
        ),
    ]

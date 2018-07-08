# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('edc_identifier', '0009_auto_20161221_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalidentifierhistory',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='historicalidentifierhistory',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalidentifierhistory',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalidentifierhistory',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='historicalidentifierhistory',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='historicalidentifierhistory',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='historicalidentifiertracker',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='historicalidentifiertracker',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalidentifiertracker',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalidentifiertracker',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='historicalidentifiertracker',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='historicalidentifiertracker',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectidentifier',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='historicalsubjectidentifier',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalsubjectidentifier',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalsubjectidentifier',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='historicalsubjectidentifier',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectidentifier',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='identifierhistory',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='identifierhistory',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifierhistory',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifierhistory',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='identifierhistory',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='identifierhistory',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='identifiertracker',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='identifiertracker',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifiertracker',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifiertracker',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='identifiertracker',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='identifiertracker',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
        migrations.AlterField(
            model_name='subjectidentifier',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='subjectidentifier',
            name='hostname_created',
            field=models.CharField(blank=True, default='mac2-2.local', help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='subjectidentifier',
            name='hostname_modified',
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='subjectidentifier',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AlterField(
            model_name='subjectidentifier',
            name='user_created',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='subjectidentifier',
            name='user_modified',
            field=edc_model_fields.fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-04 23:23

from django.db import migrations, models
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.models.audit_model_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('edc_identifier', '0001_squashed_0018_auto_20180128_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiermodel',
            name='created',
            field=models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='hostname_modified',
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='modified',
            field=models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='user_created',
            field=django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created'),
        ),
        migrations.AlterField(
            model_name='identifiermodel',
            name='user_modified',
            field=django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified'),
        ),
    ]

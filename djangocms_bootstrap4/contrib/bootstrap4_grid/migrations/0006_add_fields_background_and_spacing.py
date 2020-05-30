# Generated by Django 2.2.12 on 2020-05-30 13:23

from django.db import migrations
import djangocms_bootstrap4.contrib.bootstrap4_grid.constants
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0005_add_name_field_and_use_enum_for_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4gridcontainer',
            name='background',
            field=enumfields.fields.EnumField(default='background-none', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.constants.GridContainerBackground, max_length=255, verbose_name='Background'),
        ),
        migrations.AddField(
            model_name='bootstrap4gridcontainer',
            name='spacing',
            field=enumfields.fields.EnumField(default='spacing-none', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.constants.GridContainerSpacing, max_length=255, verbose_name='Spacing'),
        ),
    ]

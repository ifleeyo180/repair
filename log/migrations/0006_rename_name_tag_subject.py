# Generated by Django 3.2.9 on 2023-04-22 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_rename_subject_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='subject',
        ),
    ]

# Generated by Django 3.2.9 on 2023-04-22 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20230422_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='subject',
            new_name='name',
        ),
    ]

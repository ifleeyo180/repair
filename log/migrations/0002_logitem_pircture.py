# Generated by Django 3.2.9 on 2023-04-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logitem',
            name='pircture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='照片'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-03 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languagemodels',
            old_name='text',
            new_name='context',
        ),
    ]

# Generated by Django 4.2.1 on 2023-08-07 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='Scprinciple',
            new_name='Scprincipal',
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-20 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_name',
            new_name='faculty',
        ),
    ]

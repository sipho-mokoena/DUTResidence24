# Generated by Django 5.1.2 on 2024-10-20 10:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('housing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='housingadmin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='residence',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.faculty'),
        ),
        migrations.AddField(
            model_name='room',
            name='residence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.residence'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-20 10:37

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_ID', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('residence_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.residence')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=8, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=6)),
                ('home_address_street', models.CharField(max_length=255)),
                ('home_address_suburb', models.CharField(max_length=100)),
                ('home_address_city', models.CharField(max_length=100)),
                ('home_address_postal_code', models.CharField(max_length=4)),
                ('is_local', models.BooleanField()),
                ('level_of_study', models.CharField(choices=[('1st year', '1st year'), ('2nd year', '2nd year'), ('3rd year', '3rd year'), ('4th year', '4th year'), ('Postgraduate', 'Postgraduate')], max_length=20)),
                ('preferred_room_type', models.CharField(choices=[('1-sleeper', '1-sleeper'), ('2-sleeper', '2-sleeper')], max_length=10)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.faculty')),
            ],
        ),
    ]

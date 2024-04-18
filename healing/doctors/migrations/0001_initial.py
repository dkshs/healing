# Generated by Django 4.2.11 on 2024-04-18 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='specialties')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='doctors')),
                ('crm', models.CharField(max_length=30)),
                ('medical_identity_card', models.ImageField(upload_to='medical_identity_card')),
                ('zip_code', models.CharField(max_length=15)),
                ('street', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('rg', models.ImageField(upload_to='rg')),
                ('specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.specialty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
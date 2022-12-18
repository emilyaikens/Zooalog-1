# Generated by Django 3.2.5 on 2022-12-17 21:21

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
            name='Enclosure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('type', models.CharField(choices=[('TROPF', 'Tropical Freshwater'), ('TEMPF', 'Temperate Freshwater'), ('TROPM', 'Tropical Marine'), ('TEMPM', 'Temparate Marine'), ('TER', 'Terrarium'), ('E', 'Enclosure'), ('O', 'Other')], default='O', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=250)),
                ('units', models.CharField(max_length=50)),
                ('ideal_range', models.CharField(blank=True, max_length=250)),
                ('frequency', models.CharField(blank=True, max_length=250)),
                ('notes', models.CharField(blank=True, max_length=250)),
                ('enclosure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.enclosure')),
            ],
        ),
        migrations.CreateModel(
            name='ParameterLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=200)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(max_length=250)),
                ('common_name', models.CharField(max_length=250)),
                ('scientific_name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('enclosure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.enclosure')),
            ],
        ),
    ]

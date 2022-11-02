# Generated by Django 4.1.2 on 2022-10-30 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
            },
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(verbose_name='Температура')),
                ('date', models.DateField(verbose_name='Дата')),
                ('id_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature_monitoring.sensor')),
            ],
        ),
    ]
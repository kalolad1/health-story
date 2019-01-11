# Generated by Django 2.1.4 on 2019-01-11 22:32

from django.db import migrations
import django_measurement.models
import measurement.measures.distance
import measurement.measures.mass


class Migration(migrations.Migration):

    dependencies = [
        ('health_story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='height',
            field=django_measurement.models.MeasurementField(default=10, measurement=measurement.measures.distance.Distance),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=django_measurement.models.MeasurementField(default=10, measurement=measurement.measures.mass.Mass),
        ),
    ]

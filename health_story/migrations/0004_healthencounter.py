# Generated by Django 2.1.4 on 2019-01-14 00:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health_story', '0003_auto_20190111_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthEncounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physician', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=100)),
                ('type_of_encounter', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_story.Patient')),
            ],
        ),
    ]
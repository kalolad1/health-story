# Generated by Django 2.1.4 on 2019-01-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_story', '0010_auto_20190120_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='admin_mode',
            field=models.BooleanField(default=False),
        ),
    ]

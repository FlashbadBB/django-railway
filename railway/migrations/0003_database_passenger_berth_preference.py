# Generated by Django 4.0.3 on 2022-07-28 05:25

from django.db import migrations, models
import railway.models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0002_remove_database_passenger_berth_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='passenger_berth_preference',
            field=models.CharField(choices=[(railway.models.Berth_Preferences['L'], 'Lower'), (railway.models.Berth_Preferences['M'], 'Middle'), (railway.models.Berth_Preferences['U'], 'Upper')], default='Lower', max_length=1),
        ),
    ]

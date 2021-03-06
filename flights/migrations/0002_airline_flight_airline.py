# Generated by Django 4.0.1 on 2022-02-21 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=30)),
                ('airline_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='flight_airline', to='flights.airline'),
            preserve_default=False,
        ),
    ]

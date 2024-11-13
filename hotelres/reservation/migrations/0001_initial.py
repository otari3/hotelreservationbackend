# Generated by Django 5.1.3 on 2024-11-13 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotelrooms', '0001_initial'),
        ('hotels', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('price', models.IntegerField()),
                ('in_hotel', models.BooleanField()),
                ('nights', models.IntegerField()),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelrooms.hotelrooms')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'unique_together': {('check_in', 'check_out', 'hotel_id', 'room_id')},
            },
        ),
    ]

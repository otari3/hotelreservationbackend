# Generated by Django 5.1.3 on 2024-11-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelrooms',
            name='imgs',
            field=models.TextField(default='https://plus.unsplash.com/premium_photo-1661901997525-fdbfb88d8554?q=80&w=3029&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
            preserve_default=False,
        ),
    ]

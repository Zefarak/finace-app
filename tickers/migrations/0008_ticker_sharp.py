# Generated by Django 3.0.5 on 2021-04-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0007_auto_20210418_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='sharp',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=30),
        ),
    ]

# Generated by Django 3.2 on 2021-04-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0011_alter_ticker_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
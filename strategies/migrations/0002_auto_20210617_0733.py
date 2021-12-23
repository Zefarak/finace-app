# Generated by Django 3.2 on 2021-06-17 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0014_auto_20210525_0737'),
        ('strategies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrategyTicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.strategy')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_tickers', to='tickers.ticker')),
            ],
        ),
        migrations.DeleteModel(
            name='StrategyTickers',
        ),
    ]
# Generated by Django 3.0.1 on 2020-01-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0004_auto_20200102_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='fee',
            field=models.FloatField(default=0),
        ),
    ]

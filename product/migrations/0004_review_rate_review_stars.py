# Generated by Django 4.2.1 on 2023-07-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.FloatField(default=0),
        ),
    ]

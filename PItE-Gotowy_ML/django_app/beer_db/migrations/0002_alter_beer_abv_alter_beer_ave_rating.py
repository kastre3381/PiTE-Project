# Generated by Django 4.1.3 on 2022-12-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("beer_db", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="beer",
            name="ABV",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="beer",
            name="Ave_Rating",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

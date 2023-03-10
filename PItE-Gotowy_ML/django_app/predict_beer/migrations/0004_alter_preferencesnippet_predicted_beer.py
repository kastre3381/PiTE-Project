# Generated by Django 3.2.15 on 2022-12-12 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beer_db', '0002_alter_beer_abv_alter_beer_ave_rating'),
        ('predict_beer', '0003_preferencesnippet_predicted_beer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencesnippet',
            name='predicted_beer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beer_db.beer'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-22 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={},
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="taxi.manufacturer",
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="country",
            field=models.CharField(max_length=50),
        ),
    ]
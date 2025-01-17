# Generated by Django 4.2.17 on 2025-01-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animal_log",
            name="id",
        ),
        migrations.RemoveField(
            model_name="animals",
            name="id",
        ),
        migrations.AlterField(
            model_name="animal_log",
            name="name",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="animals",
            name="name",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]

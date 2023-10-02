# Generated by Django 4.2.5 on 2023-10-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Unknown Title", max_length=400)),
                ("image", models.URLField(default="No image")),
                ("date", models.CharField(default="Unknown Date", max_length=100)),
                (
                    "address",
                    models.CharField(default="Unknown Address", max_length=200),
                ),
                ("link", models.URLField(default="Unknown Link")),
                (
                    "description",
                    models.CharField(
                        default="Description not available", max_length=300
                    ),
                ),
            ],
        ),
    ]

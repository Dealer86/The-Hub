# Generated by Django 4.2.5 on 2023-10-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newsletter", "0002_remove_event_description_remove_event_end_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="image",
            field=models.URLField(default="No image"),
        ),
    ]

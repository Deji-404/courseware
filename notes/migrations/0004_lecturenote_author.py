# Generated by Django 4.2 on 2023-05-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_lecturenote_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="lecturenote",
            name="author",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

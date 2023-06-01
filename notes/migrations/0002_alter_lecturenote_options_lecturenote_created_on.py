# Generated by Django 4.2 on 2023-05-28 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lecturenote",
            options={"ordering": ["-created_on"]},
        ),
        migrations.AddField(
            model_name="lecturenote",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
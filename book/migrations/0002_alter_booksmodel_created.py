# Generated by Django 4.2.1 on 2023-06-04 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booksmodel",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 4, 8, 46, 26, 667605)
            ),
        ),
    ]

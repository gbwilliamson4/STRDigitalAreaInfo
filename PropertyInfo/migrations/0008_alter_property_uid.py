# Generated by Django 4.1.7 on 2023-03-12 03:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyInfo', '0007_alter_activities_options_activities_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d5dee1e0-9360-4234-a317-7545238e31d6'), editable=False, unique=True),
        ),
    ]

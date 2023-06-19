# Generated by Django 4.1.7 on 2023-06-11 22:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyInfo', '0009_alter_property_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytype',
            name='property',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='PropertyInfo.property'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('73e42358-69b0-4623-a752-d2b85fc7cd8a'), editable=False, unique=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-05 18:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='property',
            name='property_description',
            field=models.TextField(default=uuid.uuid4, editable=False),
        ),
    ]

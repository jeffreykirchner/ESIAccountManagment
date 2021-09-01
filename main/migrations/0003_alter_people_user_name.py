# Generated by Django 3.2.7 on 2021-09-01 23:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='user_name',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]

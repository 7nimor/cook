# Generated by Django 3.2.8 on 2023-03-25 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0018_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2023, 3, 25), null=True),
        ),
    ]

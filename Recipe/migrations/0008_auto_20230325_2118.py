# Generated by Django 3.2.8 on 2023-03-25 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0007_auto_20230325_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cook_time',
            new_name='COOK_TIME',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 25, 21, 18, 49, 434197), null=True),
        ),
    ]

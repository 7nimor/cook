# Generated by Django 4.1.7 on 2023-03-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0002_remove_recipe_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photos',
            field=models.JSONField(blank=True, null=True),
        ),
    ]

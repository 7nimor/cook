# Generated by Django 3.2.8 on 2023-03-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0021_recipe_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='content',
        ),
    ]

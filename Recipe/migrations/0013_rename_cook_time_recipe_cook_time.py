# Generated by Django 3.2.8 on 2023-03-25 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0012_remove_review_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='COOK_TIME',
            new_name='cook_time',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-25 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='photos',
        ),
    ]
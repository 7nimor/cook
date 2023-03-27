# Generated by Django 4.1.7 on 2023-03-25 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_daily', models.FloatField(blank=True, null=True)),
                ('total_fat_daily', models.FloatField(blank=True, null=True)),
                ('saturate_fat_daily', models.FloatField(blank=True, null=True)),
                ('cholesterol_daily', models.FloatField(blank=True, null=True)),
                ('sodium_daily', models.FloatField(blank=True, null=True)),
                ('total_carbohydrate_daily', models.FloatField(blank=True, null=True)),
                ('dietary_fiber_daily', models.FloatField(blank=True, null=True)),
                ('total_sugars_daily', models.FloatField(blank=True, null=True)),
                ('protein_daily', models.FloatField(blank=True, null=True)),
                ('vitamin_c_daily', models.FloatField(blank=True, null=True)),
                ('calcium_daily', models.FloatField(blank=True, null=True)),
                ('iron_daily', models.FloatField(blank=True, null=True)),
                ('potassium_daily', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('categories', models.CharField(blank=True, choices=[('lunch', 'ناهار'), ('Dinner', 'شام'), ('Breakfast', 'صبحانه'), ('Dessert', 'دسر'), ('drink', 'نوشیدنی')], max_length=200, null=True)),
                ('ingredients', models.CharField(blank=True, max_length=500, null=True)),
                ('difficulty', models.CharField(blank=True, choices=[('easy', 'آسان'), ('mid_level', 'متوسط'), ('hard', 'سخت')], max_length=200, null=True)),
                ('photos', models.TextField(blank=True, max_length=700, null=True)),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('PREP_TIME', models.IntegerField(blank=True, null=True)),
                ('COOK_TIME', models.IntegerField(blank=True, null=True)),
                ('TOTAL_TIME', models.IntegerField(blank=True, null=True)),
                ('SERVINGS', models.CharField(blank=True, max_length=500, null=True)),
                ('YIELD', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('trash', models.BooleanField(blank=True, default=False)),
                ('nutrition_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nutrition', to='Recipe.nutritionvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('reviews', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, max_length=2, null=True)),
                ('trash', models.BooleanField(blank=True, default=False)),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='Recipe.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='review',
            field=models.ManyToManyField(blank=True, related_name='reviews_1', to='Recipe.review'),
        ),
        migrations.AddField(
            model_name='nutritionvalue',
            name='recipe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='Recipe.recipe'),
        ),
    ]

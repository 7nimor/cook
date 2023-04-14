import datetime
from django.db import models
# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey("Recipe",
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='review_recipe'
                               )
    rating = models.FloatField(max_length=2, null=True, blank=True)
    trash = models.BooleanField(default=False, blank=True)
    date = models.DateField(default=datetime.datetime.now().date(), null=True, blank=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(to="Cat",null=True, blank=True,related_name='recipe_category')
    ingredients = models.TextField(null=True, blank=True)
    difficulty = models.CharField(max_length=200, null=True, blank=True)
    nutrition_value = models.ForeignKey('NutritionValue', on_delete=models.CASCADE, null=True,
                                        related_name='nutrition', blank=True)
    photos = models.JSONField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    prep_time = models.IntegerField(null=True, blank=True)
    cook_time = models.IntegerField(null=True, blank=True)
    total_time = models.IntegerField(null=True, blank=True)
    serving = models.CharField(max_length=500, null=True, blank=True)
    Yield = models.CharField(max_length=500, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    trash = models.BooleanField(default=False, blank=True)
    date = models.DateField(default=datetime.datetime.now().date(), null=True, blank=True)

    class Meta:
        verbose_name = 'دستور پخت'
        verbose_name_plural = 'دستور پخت'

    def __str__(self):
        return self.name


class NutritionValue(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    calories_daily = models.FloatField(null=True, blank=True)
    total_fat_daily = models.FloatField(null=True, blank=True)
    saturate_fat_daily = models.FloatField(null=True, blank=True)
    cholesterol_daily = models.FloatField(null=True, blank=True)
    sodium_daily = models.FloatField(null=True, blank=True)
    total_carbohydrate_daily = models.FloatField(null=True, blank=True)
    dietary_fiber_daily = models.FloatField(null=True, blank=True)
    total_sugars_daily = models.FloatField(null=True, blank=True)
    protein_daily = models.FloatField(null=True, blank=True)
    vitamin_c_daily = models.FloatField(null=True, blank=True)
    calcium_daily = models.FloatField(null=True, blank=True)
    iron_daily = models.FloatField(null=True, blank=True)
    potassium_daily = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'ارزش غذایی'
        verbose_name_plural = 'ارزش های غذایی'

    def __str__(self):
        return self.name

class Cat(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    image=models.TextField(null=True,blank=True)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE,null=True,blank=True,related_name='category_recipe')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

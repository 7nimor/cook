from django.contrib import admin
from . import models
# Register your models here.
class ReadOnly(admin.ModelAdmin):
    readonly_fields = ['trash',]


admin.site.register(models.Review)
admin.site.register(models.NutritionValue)
admin.site.register(models.Recipe)

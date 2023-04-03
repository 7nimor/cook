from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeView, ReviewViews, RandomView

router = DefaultRouter()
router.register(r'recipe', RecipeView, basename='recipe')
router.register(r'review', ReviewViews, basename='review')
router.register(r'random', RandomView, basename='random')
urlpatterns = [
    path('', include(router.urls))

]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeView, ReviewViews, RandomView,CategoryView

router = DefaultRouter()
router.register(r'recipe', RecipeView, basename='recipe')
router.register(r'review', ReviewViews, basename='review')
router.register(r'random', RandomView, basename='random')
router.register(r'category', CategoryView, basename='category')
urlpatterns = [
    path('', include(router.urls))

]

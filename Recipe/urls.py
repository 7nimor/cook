from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import RecipeView,ReviewViews
router = DefaultRouter()
router.register(r'recipe',RecipeView,basename='recipe')
router.register(r'review',ReviewViews,basename='review')

urlpatterns = [
    path('',include(router.urls))

]

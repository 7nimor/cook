from rest_framework import serializers
from .models import Recipe, Review, NutritionValue, Cat


class RecipeSerializersList(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'photos', 'difficulty', 'categories', 'cook_time','description']
        depth = 1


class RecipeSerializers(serializers.ModelSerializer):
    review = serializers.SerializerMethodField('get_review')

    class Meta:
        model = Recipe
        exclude = ('trash',)
        depth = 1

    def get_review(self, instance):
        review_list = []
        reviews = Review.objects.filter(recipe=instance)
        if reviews.count() > 0:
            for rev in reviews:
                internal_dict = {
                    "name": rev.name,
                    "reviews": rev.reviews,
                    "rating": rev.rating,
                }
                review_list.append(internal_dict)
        return review_list


class ReviewsSerializers(serializers.ModelSerializer):
    recipe = RecipeSerializersList(required=False)
    recipe_id = serializers.PrimaryKeyRelatedField(
        source='recipe',
        queryset=Recipe.objects.all()
    )

    class Meta:
        model = Review
        fields = '__all__'
        depth = 1


class NutritionValueSerializers(serializers.ModelSerializer):
    class Meta:
        model = NutritionValue
        fields = '__all__'


class Category_Serailizers(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'


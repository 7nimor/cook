from url_filter.filtersets import ModelFilterSet
from .models import Recipe, Cat


class RecipeFilterSet(ModelFilterSet):
    class Meta:
        model = Recipe


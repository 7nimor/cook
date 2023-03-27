from django.http import QueryDict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from .filterset import RecipeFilterSet
from .models import Recipe, Review
from .serializers import ReviewsSerializers, RecipeSerializers, RecipeSerializersList


# Create your views here.


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializersList
    filter_backends = [DjangoFilterBackend]
    filter_class = RecipeFilterSet
    filterset_fields = [
        'name',
        'categories',
        'ingredients',
    ]

    def list(self, request, *args, **kwargs):
        query = self.queryset.filter(trash=False)
        if 'page' in request.GET:
            stop = int(request.GET['page']) * 10
            start = stop - 10
            query = self.queryset.filter(trash=False).order_by('id')[start:stop]
            srz_data = self.serializer_class(query, many=True)
            return Response(srz_data.data, status=status.HTTP_200_OK)
        if 'type' in request.GET:
            if request.GET['type'] == 'filter':
                for item in self.filterset_fields:
                    quer = QueryDict('{0}__contains={1}'.format(item, request.GET['value']))
                    if (self.filter_class(
                            data=quer,
                            queryset=self.queryset.filter(trash=False)
                    )
                    ).filter():
                        ps = self.filter_class(data=quer, queryset=self.queryset)
                        query = ps.filter()
                        srz_data = self.serializer_class(query, many=True)
                        return Response(srz_data.data, status=status.HTTP_200_OK)
            return Response({"msg": "Not Found !"}, status=status.HTTP_403_FORBIDDEN)
        srz_data = self.serializer_class(query, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        rat = 0
        query = Recipe.objects.get(trash=False, pk=pk)
        srz_data1 = RecipeSerializers(query)
        review = Review.objects.filter(recipe__id=query.id)
        for r in review:
            if r.rating > 0:
                rat += r.rating
            else:
                pass
        if review.count() > 0:
            rating = rat / review.count()
            A_1 = "{:.1f}"
            query.rating = A_1.format(rating)
            query.save()
        else:
            query.rating = rat

        return Response(srz_data1.data, status=status.HTTP_200_OK)


class ReviewViews(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializers

    def list(self, request, *args, **kwargs):
        query = self.queryset.filter(trash=False).order_by('-id')[:10]
        srz_sata = self.serializer_class(query, many=True)
        return Response(srz_sata.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid():
            query = srz_data.create(validated_data=request.data)
            srz_data1 = self.serializer_class(query)
            return Response(srz_data1.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors)

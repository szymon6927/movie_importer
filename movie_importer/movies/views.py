from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Title
from .serializers import TitleSerializer
from .pagination import StandardResultsSetPagination


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'titles': reverse('all-titles', request=request, format=format),
        'titles-name': reverse('titles-name', request=request, format=format)
    })


class TitleListView(ListAPIView):
    """
    get:
    Return a list of movies

    Possible query_params:
    - start_year (Year)
    - genre (string)

    eg.
    /titles?start_year=1894
    or
    /titles?genre=Documentary
    """

    serializer_class = TitleSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Title.objects.order_by('original_title')

        start_year = self.request.query_params.get('date_from', None)
        genre = self.request.query_params.get('date_to', None)

        if start_year:
            queryset.filter(start_year=start_year)

        if genre:
            queryset.filter(genre__icontains=genre)

        return queryset


class TitleListBasedOnNameView(ListAPIView):
    """
    get:
    Return a list of movies based on given author name.

    Required query_params:
    - name (string)

    eg. /titles-name?name=John
    """

    serializer_class = TitleSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        queryset = Title.objects.filter(author__primary_name__icontains=name)
        return queryset

    def list(self, request, *args, **kwargs):
        name = self.request.query_params.get('name', None)

        if not name:
            return Response({"status": "Required param 'name' not found."},
                            status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset()
        serializer = TitleSerializer(queryset, many=True)
        return Response(serializer.data)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from .views import TitleListView, TitleListBasedOnNameView, api_root

schema_view = get_swagger_view(title='Movies REST API')

urlpatterns = [
    path('titles/', TitleListView.as_view(), name="all-titles"),
    path('titles-name/', TitleListBasedOnNameView.as_view(), name="titles-name"),
    path('docs/', schema_view),
    path('', api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)


from django.conf.urls import url

from django.urls import path

from .views import (
    SearchProductListView, 

    )

urlpatterns = [
    url(r'^$', SearchProductListView.as_view(), name='query'),
]

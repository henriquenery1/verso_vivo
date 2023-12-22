from django.urls import path
from contents.views import ExampleView

urlpatterns = [
    path('example/', ExampleView.as_view(), name='example-view'),
]

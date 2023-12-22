from django.urls import path

from contents.views import ContentView

urlpatterns = [
    path('', ContentView.as_view(), name='list_contents'),
]

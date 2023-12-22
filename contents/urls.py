from django.urls import path

from contents.views import ContentView, CreateContentView

urlpatterns = [
    path('', ContentView.as_view(), name='list_contents'),
    path('create/', CreateContentView.as_view(), name='create_content')
]

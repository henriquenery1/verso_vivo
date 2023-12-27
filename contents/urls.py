from django.urls import path

from contents.views import ContentView, CreateContentView, DetailContentView, TitlesContentView

urlpatterns = [
    path('', TitlesContentView.as_view(), name='titles_content'),
    path('all/', ContentView.as_view(), name='list_contents'),
    path('create/', CreateContentView.as_view(), name='create_content'),
    path('<int:content_id>/', DetailContentView.as_view(), name='detail_content'),
]

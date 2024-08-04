from django.urls import path
from .views import SearchBooksView, BookRecommendationView, index

urlpatterns = [
    path('', index, name='index'),
    path('search/', SearchBooksView.as_view(), name='search-books'),
    path('recommendations/', BookRecommendationView.as_view(), name='book-recommendations'),
]
from django.shortcuts import render

# Create your views here.
from rest_framework import status, views, generics
from rest_framework.response import Response
from .models import Book, Recommendation
from .serializers import BookSerializer, RecommendationSerializer
from .utils import fetch_books_from_google
from django.shortcuts import render

class SearchBooksView(views.APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        books_data = fetch_books_from_google(query)
        books = []
        for book_data in books_data:
            volume_info = book_data['volumeInfo']
            book = {
                'title': volume_info.get('title'),
                'author': ', '.join(volume_info.get('authors', [])),
                'description': volume_info.get('description', ''),
                'cover_image': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                'rating': volume_info.get('averageRating', 0),
            }
            books.append(book)
        return Response(books)

class BookRecommendationView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

def index(request):
    return render(request, 'index.html')

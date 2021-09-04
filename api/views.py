from rest_framework import generics

from books.models import Book
from .serializers import BooksSerializer

class BooksApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
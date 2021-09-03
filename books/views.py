from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

class BookList(ListView):
    model = Book
    template_name = 'books/books_list.html'

    context_object_name = 'books'
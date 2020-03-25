from django.shortcuts import render
from .models import Book

# Create your views here.
class ModelNameList(ListView):
    model = Book
    context_object_name = 'book'
    template_name='book_list.html'
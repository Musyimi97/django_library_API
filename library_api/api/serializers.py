from rest_framewok import serializers
from library_api.books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = ('title', 'subtitle', 'author', 'isbn')
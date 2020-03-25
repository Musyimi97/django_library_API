from django.test import TestCase
from .models import Book

# Create your tests here.

class BookTestCase(TestCase):
    @classmethod

    def setUpTestData(cls):
        Book.objects.create(title = "gucci", subtitle= 'clothe_brand', author='Collins Musyimi', isbn="300-2908-1997")

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name =f'{book.title}'
        self.assertEqual(expected_object_name, 'gucci')
    def test_subtitle_content(self):
        book = Book.objects.get(id=1)
        expected_object_name=f'{book.subtitle}'
        self.assertEqual(expected_object_name, 'clothe_brand')
    def test_author_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.author}'
        self.assertEqual(expected_object_name, 'Collins Musyimi')
    def test_isbn_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.isbn}'
        self.assertEqual(expected_object_name, '300-2908-1997')

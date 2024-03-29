from nsApp.models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'

class AuthorSerialiser(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model=Author
        fields = '__all__'


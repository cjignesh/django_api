from django.shortcuts import render
from rest_framework import generics
from nsApp.models import Author, Book
from nsApp.serializer import AuthorSerialiser, BookSerializer
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
# Create your views here.

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerialiser
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerialiser

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

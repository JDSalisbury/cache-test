from django.shortcuts import render
from faker import Faker

from rest_framework import status

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import generics, viewsets


class BlogView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()


class DataBlastView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def add_data(self, request, pk, *args, **kwargs):
        for x in range(pk):
            fake = Faker()
            Blog.objects.create(
                name=fake.name(), slug=fake.slug(), body=fake.text())

        return Response(status=status.HTTP_201_CREATED)


class BlogListView(APIView):
    def get(self, slug):
        try:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

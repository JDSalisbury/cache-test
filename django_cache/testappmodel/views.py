from django.shortcuts import render
from faker import Faker

from rest_framework import status

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog
from .tasks import data_dump, send_email_task
from rest_framework import generics, viewsets


class BlogView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class EmailView(viewsets.ModelViewSet):

    def email(self, request):
        task = send_email_task.delay()
        context = {}
        context['task_id'] = task.id
        context['task_status'] = task.status

        return Response(context)


class DataBlastView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def add_data(self, request, pk, *args, **kwargs):
        try:
            task = data_dump.delay(pk)
            context = {}
            context['task_id'] = task.id
            context['task_status'] = task.status

            return Response(context)
        except Exception:  # pragma: no cover
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlogListView(APIView):
    def get(self, slug):
        try:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:  # pragma: no cover
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

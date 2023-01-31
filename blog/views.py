from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AllBlogSerializer
from .models import Blog


class AllBlogs(APIView):

    def get(self, request):
        all_blog = Blog.objects.all()
        all_blog_serializer = AllBlogSerializer(instance=all_blog, many=True)
        return Response(data=all_blog_serializer.data, status=status.HTTP_200_OK)



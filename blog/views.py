from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import

class AllBlogs(APIView):

    def get(self,request):
        ...

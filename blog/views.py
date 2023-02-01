from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import BlogSerializer
from .models import Blog,Like,View,BlogCategory


class AllBlogs(APIView):

    def get(self, request):
        all_blog = Blog.objects.all()
        all_blog_serializer = BlogSerializer(instance=all_blog, many=True)
        return Response(data=all_blog_serializer.data, status=status.HTTP_200_OK)

class SingleBlog(APIView):

    def get(self,request,blog_id:int):

        if blog_id == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        single_blog = Blog.objects.filter(id = blog_id).first()
        if not single_blog:
            return Response(status=status.HTTP_404_NOT_FOUND)

        single_blog_serializer = BlogSerializer(instance=single_blog,many=False)
        return Response(data = single_blog_serializer.data,status=status.HTTP_200_OK)


class SearchBlog(APIView):

    def get(self,request,query:str):

        if query == "":
            return Response(status=status.HTTP_200_OK)

        searched_blogs = Blog.objects.filter(Q(title__icontanis = query) | Q(short_description__icontains = query) | Q(text__icontains = query))
        searched_blogs_serializer = BlogSerializer(instance=searched_blogs,many=True)

        return Response(data = searched_blogs_serializer.data,status=status.HTTP_200_OK)


class FilterBlog(APIView):
    # start time and end time format : MM/DD/YYYY
    def get(self,request,start_time:str,end_time:str):
        ...

    


class BlogWithCategory(APIView):

    def get(self,request,category_id:int):

        if category_id == 0:
            return Response(status = status.HTTP_404_NOT_FOUND)

        category = BlogCategory.objects.filter(id = category_id).first()
        if not category:
            return Response(status = status.HTTP_404_NOT_FOUND)

        blogs_with_category = Blog.objects.filter(category = category)
        blogs_with_category_serializer = BlogSerializer(instance = blogs_with_category)
        return Response(data = blogs_with_category_serializer.data,status = status.HTTP_200_OK)



class LikeBlog(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, blog_id: int):

        if blog_id == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        blog = Blog.objects.filter(id=blog_id).first()
        if not blog:
            return Response(status=status.HTTP_404_NOT_FOUND)

        like = Like.objects.filter(blog = blog,user = request.user)
        if not like:
            like = Like(blog = blog,user = request.user)
        else:
            like.first().delete()
        like.save()

        return Response(status = status.HTTP_200_OK)

class ViewBlog(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request,blog_id:int):

        if blog_id == 0:
            return Response(status = status.HTTP_404_NOT_FOUND)

        blog = Blog.objects.filter(id = blog_id).first()
        if not blog:
            return Response(status = status.HTTP_404_NOT_FOUND)

        view = View.objects.filter(blog = blog,user = request.user)
        if not view:
            view = View(blog = blog,user = request.user)
        else:
            view.first().delete()
        view.save()

        return Response(status=status.HTTP_200_OK)

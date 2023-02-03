from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import BlogSerializer,CommentSerializer
from .models import Blog,Like,View


class AllBlogs(APIView):

    def get(self, request):
        all_blog = Blog.objects.filter(active = True).all()
        all_blog_serializer = BlogSerializer(instance=all_blog, many=True)

        return Response(data=all_blog_serializer.data, status=status.HTTP_200_OK)

class SingleBlog(APIView):

    def get(self,request,blog_id:int):

        if blog_id == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        single_blog = Blog.objects.filter(id = blog_id,active = True).first()
        if not single_blog:
            return Response(status=status.HTTP_404_NOT_FOUND)

        single_blog_serializer = BlogSerializer(instance=single_blog,many=False)
        return Response(data = single_blog_serializer.data,status=status.HTTP_200_OK)


class SearchBlog(APIView):

    def get(self,request,query:str):
        
        if query == "":
            return Response(status=status.HTTP_200_OK)
        
        searched_blogs = Blog.objects.filter(Q(title__icontains  = query) | Q(short_description__icontains = query) | Q(text__icontains = query))
        searched_blogs_serializer = BlogSerializer(instance=searched_blogs,many=True)

        return Response(data = searched_blogs_serializer.data,status=status.HTTP_200_OK)




class LikeBlog(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, blog_id: int):

        if blog_id == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        blog = Blog.objects.filter(id=blog_id,active = True).first()
        if not blog:
            return Response(status=status.HTTP_404_NOT_FOUND)

        like = Like.objects.filter(blog = blog,user = request.user)
        if not like:
            like = Like(blog = blog,user = request.user)
            like.save()
        else:
            like.first().delete()

        return Response(status = status.HTTP_200_OK)

class ViewBlog(APIView):


    def get(self,request,blog_id:int):
        from tools.net.network import Network
        
        if blog_id == 0:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        blog = Blog.objects.filter(id = blog_id,active = True).first()
        if not blog:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        user_ip:str = Network.get_user_ip(request)
        if request.user.is_authenticated:
            views = View.objects.filter(Q(blog = blog) & (Q(user = request.user) | Q(ip = user_ip)))
            if not views:
                View.objects.create(blog = blog,user = request.user,ip = user_ip)
        else:
            views = View.objects.filter(blog = blog,ip = user_ip)
            if not views:
                View.objects.create(blog = blog,ip = user_ip)
        return Response(status = status.HTTP_200_OK)
            
        

class CommentBlog(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self,request,blog_id:int):
        
        comment_serializer = CommentSerializer(data = request.data,user = request.user,blog_id = blog_id)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(data = {"message" : "Comment Saved Successfully ..."},status=status.HTTP_200_OK)
        return Response(data = comment_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

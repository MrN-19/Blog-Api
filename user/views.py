from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from .serializers import UserRegisterSerializer,UserLoginSerializer
from blog.serializers import BlogSerializerFromUser

from django.contrib.auth import login,logout

class UserRegister(APIView):

    def post(self,request):
        user_register_serializer = UserRegisterSerializer(data = request.data)
        if user_register_serializer.is_valid():
            user_register_serializer.save()

            token = Token.objects.create(user = user_register_serializer.user)

            return Response({"message" : "user registred successfully ...","token" : token.key},status=status.HTTP_200_OK)
        return Response(user_register_serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
class UserLogin(APIView):

    def post(self,request):
        user_login_serializer = UserLoginSerializer(data = request.data)
        if user_login_serializer.is_valid():
            login(request,user_login_serializer.user)
            return Response({
                "message" : "Login Done ! :)",
                "token" : user_login_serializer.token
            })
        return Response(user_login_serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
class UserLogout(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request):

        Token.objects.filter(user = request.user).delete()
        return Response(status=status.HTTP_200_OK)
    

class NewBlog(APIView):

    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def post(self,request):

        blog_serializer_from_user = BlogSerializerFromUser(data = request.data,user = request.user)

        if blog_serializer_from_user.is_valid():
            blog_serializer_from_user.save()

            data = {
                "message" : "Your Blog Added Successfully ..."
            }

            return Response(data,status=status.HTTP_200_OK)
        
        return Response(data = blog_serializer_from_user.error_messages,status=status.HTTP_400_BAD_REQUEST)
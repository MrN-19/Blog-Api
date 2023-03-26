from typing import Dict,Any

from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Blog, BlogComment,BlogCategory


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    user_name = serializers.CharField(source="user.username")

    likes_count = serializers.IntegerField(source = "likes.count")
    view_count = serializers.IntegerField(source = "views.count")

    comments = CommentsSerializer(many=True, read_only=True)


    class Meta:
        model = Blog
        exclude = ("user",)



class CommentSerializer(serializers.Serializer):

    def __init__(self, instance=None, data=..., **kwargs):
        self.__blog_id:int = kwargs.get("blog_id",0)
        self.__user = kwargs.get("user",None)
        super().__init__(instance, data, **kwargs)


    comment_text = serializers.CharField(required = True,error_messages = {
        "required" : "Please Enter Comment Text",
    })

    def create(self, validated_data):
        text = validated_data.get("comment_text")
        blog = Blog.objects.filter(id = self.__blog_id).first()
        return BlogComment(
            text = text,
            blog = blog,
            user = self.__user
        )
    
class BlogSerializerFromUser(serializers.Serializer):

    def __init__(self, user,instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.__user = user

    @property
    def user(self) -> User:
        return self.__user

    category_id = serializers.IntegerField(default=0)

    title = serializers.CharField(max_length = 150,error_messages = {
        "required" : "Please Enter Title",
        "max_length" : "Entred Title is too long"
    })

    short_describtion = serializers.CharField(max_length = 500,error_messages = {
        "required" : "Please Enter Short Describtion",
        "max_length" : "Entred Short Describtion is too long"
    })

    picture = serializers.ImageField(error_messages = {
        "blank" : "Please Enter Picture"
    })

    text = serializers.CharField(error_messages = {
        "required" : "Please Enter Text !"
    })
    
    def create(self, validated_data:Dict[str,Any]):

        category_id:int = validated_data.get("category_id",0)

        if category_id == 0:
            raise serializers.ValidationError("Category Id is not Valid ... !")
        if not self.__user:
            raise serializers.ValidationError("User Is Not Valid ... !")

        category = BlogCategory.objects.filter(id = category_id).first()

        if not category:
            raise serializers.ValidationError("Category Not Found ... !")

        title:str = validated_data.get("title","")
        short_describtion:str = validated_data.get("short_describtion","")
        text:str = validated_data.get("text","")

        picture = validated_data.get("picture",None)

        new_blog = Blog(
            user = self.__user,
            category = category,
            title = title,
            short_description = short_describtion,
            text = text,
            picture = picture
        )
        
        return new_blog
        

from rest_framework import serializers

from .models import Blog, BlogComment


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    user_name = serializers.CharField(source="user.username")
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        exclude = ("user",)

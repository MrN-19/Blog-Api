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
    
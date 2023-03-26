from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):
    title = models.CharField(max_length = 120,verbose_name = "Category Name")
    picture = models.ImageField(upload_to = "blog-category/pictures",null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory,on_delete = models.CASCADE,verbose_name = "Category Name",null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", null=True)
    title = models.CharField(max_length=150, verbose_name="Blog Title")
    short_description = models.CharField(max_length=500, verbose_name="Short Describtion")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="Publish Date")
    picture = models.ImageField(upload_to="blog/pictures")
    text = RichTextUploadingField(verbose_name="Text Of Blog",null=True)
    active = models.BooleanField(default=True,verbose_name="Blog Activation")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class LikeView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User",null=True)

    def __str__(self):
        return f"{self.blog.title} ---- {self.user.username}"


class Like(LikeView):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog", related_name="likes")

    class Meta:
        verbose_name = "Blog Like Count"
        verbose_name_plural = "Blog Likes Count"


class View(LikeView):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog", related_name="views")
    ip = models.CharField(max_length=15,verbose_name="User Ip",null=True)
    class Meta:
        verbose_name = "Blog View Count"
        verbose_name_plural = "Blogs View Count"


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog",related_name="comments")
    text = models.TextField(max_length=1000, verbose_name="Comment Text")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Comment Create Date")

    def __str__(self):
        return f"{self.user.username} -- {self.blog.title}"
    

    class Meta:
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comments"

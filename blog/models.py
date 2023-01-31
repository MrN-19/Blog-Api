from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User",null=True)
    title = models.CharField(max_length=150, verbose_name="Blog Title")
    short_description = models.CharField(max_length=500, verbose_name="Short Describtion")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="Publish Date")
    picture = models.FileField(upload_to="blog/pictures", validators=[
        FileExtensionValidator(allowed_extensions=(".jpg", ".png", "jpeg"), message="This File is not Valid")
    ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class LikeView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    def __str__(self):
        return f"{self.blog.title} ---- {self.user.username}"


class Like(LikeView):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog",related_name="likes")

    class Meta:
        verbose_name = "Blog Like Count"
        verbose_name_plural = "Blog Likes Count"


class View(LikeView):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog", related_name="views")

    class Meta:
        verbose_name = "Blog View Count"
        verbose_name_plural = "Blogs View Count"

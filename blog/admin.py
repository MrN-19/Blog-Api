from django.contrib import admin
from . import models


class BlogAdmin(admin.ModelAdmin):
    list_filter = ("title", "user")


admin.site.register(models.Blog, BlogAdmin)


class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ("user", "blog")


admin.site.register(models.Like, LikeAdmin)


class ViewAdmin(admin.ModelAdmin):
    readonly_fields = ("user", "blog")


admin.site.register(models.View, ViewAdmin)


class CommentBlogAdmin(admin.ModelAdmin):
    readonly_fields = ("create_date",)


admin.site.register(models.BlogComment, CommentBlogAdmin)

from django.urls import path
from .views import AllBlogs,LikeBlog,ViewBlog,SingleBlog,SearchBlog

urlpatterns = [
    path("blogs",AllBlogs.as_view(),name="allblogs"),
    path("like-blog/<int:blog_id>",LikeBlog.as_view(),name="likeblog"),
    path("view-blog/<int:blog_id>",ViewBlog.as_view(),name="viewblog"),
    path("blog/<int:blog_id>",SingleBlog.as_view(),name="singleblog"),
    path("search/<str:query>",SearchBlog.as_view(),name="searchblog"),
]
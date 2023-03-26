from django.urls import path
from .views import AllBlogs,LikeBlog,ViewBlog,SingleBlog,SearchBlog,BlogWithCategory,CommentBlog,LastBlogs


app_name:str = "blog"

urlpatterns = [
    path("",LastBlogs.as_view(),name="lastblogs"),
    path("blogs",AllBlogs.as_view(),name="allblogs"),
    path("like-blog/<int:blog_id>",LikeBlog.as_view(),name="likeblog"),
    path("view-blog/<int:blog_id>",ViewBlog.as_view(),name="viewblog"),
    path("blog/<int:blog_id>",SingleBlog.as_view(),name="singleblog"),
    path("search/<str:query>",SearchBlog.as_view(),name="searchblog"),
    path("blog-comment/<int:blog_id>",CommentBlog.as_view(),name="commentblog"),
    path("blog-category/<int:category_id>",BlogWithCategory.as_view(),name="blogwithcategory"),
]
    


from django.urls import path

from .views import UserLogin,UserLogout,UserRegister,NewBlog,UserBlogs,DeleteBlog


app_name:str = "user"

urlpatterns = [
    path("register",UserRegister.as_view(),name="userregister"),
    path("login",UserLogin.as_view(),name="userlogin"),
    path("logout",UserLogout.as_view(),name="logout"),
    path("new-blog",NewBlog.as_view(),name="newblog"),
    path("user-blogs",UserBlogs.as_view(),name="userblogs"),
    path("delete-blog/<int:blog_id>",DeleteBlog.as_view(),name="deleteblog"),
]
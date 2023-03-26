from django.urls import path

from .views import UserLogin,UserLogout,UserRegister,NewBlog


app_name:str = "user"

urlpatterns = [
    path("register",UserRegister.as_view(),name="userregister"),
    path("login",UserLogin.as_view(),name="userlogin"),
    path("logout",UserLogout.as_view(),name="logout"),
    path("new-blog",NewBlog.as_view(),name="newblog"),
]
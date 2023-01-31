from django.urls import path
from .views import AllBlogs

urlpatterns = [
    path("blogs",AllBlogs.as_view(),name="allblogs"),
]
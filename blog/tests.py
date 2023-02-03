from os import path

from django.test import TestCase,Client
from django.contrib.auth.models import User
from simple_blog.settings import BASE_DIR

from blog.models import Blog

class BlogTestCase(TestCase):

    __SUCCESS_STATUS_CODE:int = 200

    def setUp(self) -> None:
        self.__client = Client(enforce_csrf_checks=True)

        self.__test_user = User(username = "testuser",first_name = "mohammadreza",last_name = "nazif")
        self.__test_user.set_password("123456789")
        self.__test_user.save()


        blog_picture_path:str = path.join(str(BASE_DIR),"static","test_files","test.jpg")
        test_blog = Blog(user = self.__test_user,title = "Test Title",short_description = "Test Short Description",text = "Test text",picture = blog_picture_path)
        test_blog.save()

    def test_all_blogs(self):
        response = self.__client.get("/blogs")
        self.assertEqual(response.status_code,self.__SUCCESS_STATUS_CODE)

    def test_single_blog(self):
        response = self.__client.get("/blog/1")
        self.assertEqual(response.status_code,self.__SUCCESS_STATUS_CODE)

    def test_search_blog(self):
        response = self.__client.get("/search/m")
        self.assertEqual(response.status_code,self.__SUCCESS_STATUS_CODE)

    def test_like_blog(self):
        self.__client.login(username = "testuser",password = "123456789")

        response = self.__client.get("/like-blog/1")
        self.assertEqual(response.status_code,self.__SUCCESS_STATUS_CODE)

    def test_view_blog(self):
        response = self.__client.get("/view-blog/1")
        self.assertEqual(response.status_code,self.__SUCCESS_STATUS_CODE)

    def test_blog_comment(self):
        self.__client.login(username = "testuser",password = "123456789")
        
        data_to_send = {
            "comment_text" : "this is a Simple Text"
        }
        response = self.__client.post("/blog-comment/1",data_to_send)
        self.assertEqual(response.status_code,self.__SUCCESS_STATUS_CODE)


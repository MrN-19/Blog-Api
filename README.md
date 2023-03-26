# Simple Blog Api

this is a blog api project has written by python and django web framework that can help front end developers to run their project 

this project has basic options of a weblog website such as 

* list of all blogs
* get blogs by categories
* search blog by parameter
* single blog 
* like the blog
* visit the blog
* add comment to each blog
* show comments for blog
* ...

## How to Start Project ?

1. this is django project so you need to install python on you machine
2. after installing python you need to activate virtual environment of project like below :
    * on linux based operation systems
        * `source env/Scripts/activate`
    * on windows os
        * `env/Scripts/activate.exe`
3. after activating project you should install packages and requirements things by this below command :
    * `python/python3 -r requirements.txt`
    * python3 is for linux based os
    * python is for windows os
    * notice that you should enter above command when you are in directory that requirements.txt is in that
4. for running project you should enter below command : 
    * for linux : `python3 manage.py runserver`
    * for windows : `python manage.py runserver`
5. project will run in `http://127.0.0.1:8000`
6. and you can work with this url and send any http request that needed

## How to Use Of Project ?

this project is simple that there are list of urls that you can send request and get data

### list Of urls
* `http://127.0.0.1:8000`
    * this path gives us recent blogs have just added
* `http://127.0.0.1:8000/blogs` 
    * this path gives us all blogs in database
* `http://127.0.0.1:8000/blog/{blog id}` 
    * this path gives a single blog information by sending blog id in url like that
* `http://127.0.0.1:8000/search/{query}` 
    * this path gives us list of blogs by query sent in url
    * query searched in (title of blog) , (short description of blog) , (text of blog)
* `http://127.0.0.1:8000/like-blog/{blog id}`
    * in this url you can like a blog by sending blog id in url
    * this service needs user authentication , for authenticating you should use of commands that we talked about in below
* `http://127.0.0.1:8000/view-blog/{blog id}`
    * in this url you can set blog visit by sending blog id
* `http://127.0.0.1:8000/register`
    * in this url you can register a new user
    * parameters you should send are
        1. username -> maximum length is 150 characters
        2. password -> maximum length is 150 and minimum length is 8 characters
    * as response you will recive a json that includes these keys
        * a message that says register was successfull
        * a token that you should store it in browser storage or anywhere you can to send it to server for login
* `http://127.0.0.1:8000/login`
    * in this url you can login requirements thing is like register 
* `http://127.0.0.1:8000/logout`
    * in this url you can logout
    * when you logout your token will delete
    * for logout you should were login before else you cant do logout action
* `http://127.0.0.1:8000/user-blogs`
    * this url will return blogs that current user have published and for using of this 
    service you should be signed in (you can see how to sign in in below)

* `http://127.0.0.1:8000/new-blog`

    * this is a post request , that each user can publish own blog
    * data you should send 

        1. title -> string field (max_length = 150 Characters)
        2. short_describtion -> string field (max_length = 500 Characters)
        3. text -> string field with no limit in Characters
        4. picture -> this is file field , and you should send media file (image, jpeg,jpg,...)
        5. category_id -> this int field and you should send id of category

    * you send these data to above url

* `http://127.0.0.1:8000/delete-blog/{blog_id:int}`

    * this url will delete user blog
    
    * in url parameter you should send `blog id`
    * blog id is type of integer


## Blog Fields
    
* id
* first_name
* last_name
* user_name
* likes_count
* view_count
* comments
* title
* short_description
* publish_date
* picture
* text
* active


## How to add new Blog ?
in django we have a default admin panel that you can control your web app settings and data

1. create a super user by below command
    * linux : `python3 manage.py createsuperuser`
    * windows : `python manage.py createsuperuser`
    * after above command you enter username , email is optional , and password
2. after creating a super user you can enter to admin panel in `http://127.0.0.1:8000/admin`
3. now you are in admin panel and can edit data

# How to Use Of Urls that need user authentication ?

for using urls that need user to be loged in system you should do below steps :

1. at the first by using of login url you should login to system
2. after loging server gives you a token that is unique for each user
3. now after getting token you should store in a local database or browser storage or anywhere
4. now for using of api's that need to user authentication you should send this token in header when you are sending request like this

    * in Header of request do like this
    * Authorization : Token `token key`


# Hope to Enjoy


    


    

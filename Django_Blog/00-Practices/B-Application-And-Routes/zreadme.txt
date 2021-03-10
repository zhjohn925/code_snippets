
# Note: single project directory can holds multiple apps.
#       Also, you can take single app add to multiple projects

##############################################################
# Project directory:  django_project/django_project
# App directory: django_project/blog
##############################################################

# create 'blog' app
1. django_project>  python manage.py startapp blog       # blog package is created

# we can use 'tree' command to view the directory structures

2. django_project\blog\views.py
    - add home()
    - add about()

3. blog\urls.py
    - add the relative path '' route to views.home()
    - add the relative path 'about/' route to views.about()
        path('', views.home, name='blog-home'),    ####<<<<<<<<<<<###   
                                                                   #^   
4. add 'blog' urls into project urls                               #^ 
   django_project/urls.py                                          #^
   - first way:                                                    #^
     path('blog/', include('blog.urls')),          ####>>>>>>>>>>>###
     # Note: the url with blog/ and blog/* would map to this path
     # --> http://127.0.0.1:8000/blog mapped to 'blog.urls' --> then "views.home"
     # --> http://127.0.0.1:8000/blog/about mapped to 'blog.urls' --> then "views.about"
     OR:
   - second way  
     path('', include('blog.urls')),  
     # --> http://127.0.0.1:8000  mapped to 'blog.urls' --> then "views.home" 

5. Test the website
   # if web server not UP:  django_project> python manage.py runserver
   http://127.0.0.1:8000/blog              #(first way)
   http://127.0.0.1:8000/blog/about        #(first way)
   http://127.0.0.1:8000/            #(second way)
   http://127.0.0.1:8000/about       #(second way)


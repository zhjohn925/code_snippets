
1. add 'blog' app into project installed list; so django knows where to look
    for blog template files, and blog database later.
    - The recommended way is to add blog configuration to project installed list.
      ie. add 'BlogConfig' in blog/apps.py to django_project/settings.py
            INSTALLED_APPS = [
                'blog.apps.BlogConfig',
                :::::::::
            ]

2. create django_project/blog/templates
3. create django_project/blog/templates/blog

# Templates directory structure:
    blog -> templates -> blog -> templates.html

4. create templates:
    blog/templates/blog/home.html
    blog/templates/blog/about.html

5. modify blog/views.py to render templates (home.html, about.html)

6. test website
    http://127.0.0.1:8000/           
    http://127.0.0.1:8000/about      


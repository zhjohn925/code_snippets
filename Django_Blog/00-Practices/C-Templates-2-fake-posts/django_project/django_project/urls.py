"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# This is project urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    ######################################################
    #In the case of multiple apps in a project,
    # the app 'blog' as example.
    #
    #blog/  and blog/* are mapped to 'blog.urls'
    #ie.   http://127.0.0.1:8000/blog 
    #      http://127.0.0.1:8000/blog/about
    ######################################################
    #path('blog/', include('blog.urls')),   

    ######################################################
    #In the case of only one app ('blog') in a project, 
    #    
    #/  and /* are mapped to 'blog.urls'
    #ie.   http://127.0.0.1:8000/
    #      http://127.0.0.1:8000/about
    ######################################################
    path('', include('blog.urls')),        

]

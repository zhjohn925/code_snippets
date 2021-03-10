from django.shortcuts import render
from django.http import HttpResponse

posts = [
    { 'author': 'Mike', 
      'title': 'Blog Post 1',
      'content': 'First post content',
      'date_posted': 'March 7, 2021'  
    },
    { 'author': 'Jeff', 
      'title': 'Blog Post 2',
      'content': 'Second post content',
      'date_posted': 'March 8, 2021'  
    }
]

def home(request) :
    context = { 'posts': posts }
    return render(request, 'blog/home.html', context)

def about(request) :
    return render(request, 'blog/about.html', {'title': 'About'})
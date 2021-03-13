from django.contrib import admin
from .models import Post

# Register your models here.

# add Post in admin page (127.0.0.1:8000/admin)
admin.site.register(Post)
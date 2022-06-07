from django.contrib import admin
from .models import BlogPost, Blogger

admin.site.register(Blogger)
admin.site.register(BlogPost)
from django.contrib import admin
from .models import BlogPost, Blogger, Comment

admin.site.register(Blogger)
admin.site.register(BlogPost)
admin.site.register(Comment)
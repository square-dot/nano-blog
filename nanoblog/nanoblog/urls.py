from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", views.home, name="home"),
    path("", RedirectView.as_view(url="blog/", permanent=True)),
    path("blog/bloggers/", views.Bloggers.as_view(), name="bloggers"),
    path("blog/blogger/<int:pk>", views.BloggerView.as_view(), name = "blogger"),
    path("blog/blogposts/", views.BlogPosts.as_view(), name="blogposts"),
    path("blog/blogpost/<int:pk>/", views.BlogPostView.as_view(), name="blogpost"),
    path("blog/blogpost/<int:pk>/create", views.BlogPostView.as_view(), name="create_blogpost"),
] + [
    path("", include('django.contrib.auth.urls')),
]

from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", views.home, name="home"),
    path("", RedirectView.as_view(url="blog/", permanent=True)),
    path("authors/", views.Authors.as_view(), name="authors"),
    path("blogentries/", views.BlogEntries.as_view(), name="blogentries"),
] + [
    path("login/", views.login, name="login"),
    path("loggedout/", views.login, name="loggedout"),
]

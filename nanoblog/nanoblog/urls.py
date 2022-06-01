from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", views.home, name="home"),
    path("", RedirectView.as_view(url="blog/", permanent=True)),
    path("authors/", views.Authors.as_view(), name="authors"),
    path("blogentries/", views.BlogEntries.as_view(), name="blogentries"),
] + [
    path("", include('django.contrib.auth.urls')),
]

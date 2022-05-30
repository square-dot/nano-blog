from django.shortcuts import render
from django.views.generic import ListView
from nanoblog.models import Author, BlogEntry

def home(request):
    context = {}
    return render(request, "home.html", context=context)

def login(request):
    return render(request, "login.html", context = {})


class Authors(ListView):
    model = Author
    paginate_by = 5


class BlogEntries(ListView):
    model = BlogEntry
    paginate_by = 20
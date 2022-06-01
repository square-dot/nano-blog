from django.shortcuts import render
from django.views.generic import ListView
from nanoblog.models import Author, BlogEntry
from django.contrib.auth import authenticate, login

def home(request):
    context = {}
    return render(request, "home.html", context=context)


class Authors(ListView):
    model = Author
    paginate_by = 5


class BlogEntries(ListView):
    model = BlogEntry
    paginate_by = 20


def login_page(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "home.html", context = {"message" : "login please"})
    else:
        return render(request, "login.html", context={"message" : "login failed"})


from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from nanoblog.models import Blogger, BlogPost, Comment


def home(request):
    context = {}
    return render(request, "home.html", context=context)

class BloggerView(DetailView):
    model = Blogger
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blogposts'] = BlogPost.objects.filter(blogger=ctx["object"])
        return ctx

def new_blog(request):
    return render(request, "new_blog.html", context={})

class BlogPostView(DetailView):
    model = BlogPost
    
    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['comments'] = Comment.objects.filter(blogpost=ctx["object"])
        return ctx

class Bloggers(ListView):
    model = Blogger
    paginate_by = 5


class BlogPosts(ListView):
    model = BlogPost
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


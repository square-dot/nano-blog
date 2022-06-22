from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import datetime


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shortbio = models.TextField(max_length=2000)

    def __str__(self):
        return self.user.get_full_name()

    def get_aboslute_url(self):
        print(f"Returning absolute url for blogger {self.id}")  # type: ignore
        return reverse("blogger", args=[str(self.id)])  # type: ignore

    class Meta:
        ordering = ["user"]


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __str__(self):
        return f"{self.title}"

    def get_aboslute_url(self):
        print(f"Returning absolute url for blogpost {self.id}")  # type: ignore
        return reverse("blogpost", args=[str(self.id)])  # type: ignore

class Comment(models.Model):
    text = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now, editable=False)

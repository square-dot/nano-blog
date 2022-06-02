from django.contrib.auth.models import User
from django.db import models


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shortbio = models.TextField(max_length=2000)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ["user"]


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogentry = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

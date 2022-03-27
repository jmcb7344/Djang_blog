from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    #autor = models.ForeignKey()

    def __str__(self):
        return self.title

class Coment(models.Model):
    #usuario = models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    coment = models.TextField()

    def __str__(self):
        return self.user.username

class Like(models.Model):
    #usuario = models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Vistas(models.Model):
    #usuario = models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
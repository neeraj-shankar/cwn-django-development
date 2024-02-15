from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Author model (One-to-One relationship with User)
class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


# Category model (Many-to-Many relationship with Post)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Post model (One-to-Many relationship with Author and Many-to-Many relationship with Category)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name="cls_title_idx")
        ]

    def __str__(self):
        return self.title


# Comment model (One-to-Many relationship with Post and ForeignKey to User for the author)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
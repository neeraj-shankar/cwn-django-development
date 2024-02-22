from django.db import models

from author.models import Author
from app.models import Category

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name

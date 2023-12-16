from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    name = models.CharField("Name",max_length=200)
    img = models.ImageField("Cover Photo", upload_to="port_pics")
    desc = RichTextField(verbose_name="Description", null=True, blank= True)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Phone",max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    type = models.CharField(verbose_name="Service Name", max_length=200)
    desc = RichTextField(verbose_name="Description", null=True, blank= True)

    def __str__(self):
        return self.type

class Skill(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    desc = RichTextField(verbose_name="Description", null=True, blank= True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    writer = models.CharField(verbose_name="Title",max_length=200)
    feedback = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.writer
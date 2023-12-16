from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
#****************************** Blog Category******************
class Category(models.Model):
    sno_category = AutoField(primary_key=True)
    img = models.ImageField(verbose_name="Cover Photo", null=True,blank =True, upload_to="cat_pics/")
    title = models.CharField(verbose_name="Title", max_length=200)
    desc = RichTextField(verbose_name="Description", null=True, blank= True)
    slug = models.SlugField(unique=True, verbose_name="Slug Field", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


#****************************** Blog List******************

class Author(models.Model):
    author_name = models.CharField(verbose_name="Author Name", max_length=200)
    about = models.TextField("Author Description",blank=True, null=True)
    img = models.ImageField("Author Cover", upload_to="author_pics",blank=True,null=True)
    

    def __str__(self):
        return self.author_name

    
class Post(models.Model):
    sno_post = AutoField(primary_key=True)
    date = models.DateField(verbose_name="Date of Posting", auto_now_add=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    category = models.CharField(verbose_name="Category", max_length=200)
    img = models.ImageField(verbose_name="Cover Photo", null=True,blank =True,upload_to="post_pics/")
    title = models.CharField(verbose_name="Title", max_length=200)
    #post_desc1 = models.TextField(verbose_name="First Paragraph")
    desc = RichTextField(verbose_name="Description", null=True, blank= True)
    slug = models.SlugField(unique=True, verbose_name="Slug Field", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title   


class Comment(models.Model):
    sno_comment = AutoField(primary_key=True)
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField("Your Name", max_length=200)
    email = models.EmailField("Email", max_length=200)
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    parent= models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class PostCover(models.Model):
    heading = models.CharField("Heading", max_length=200)
    desc = RichTextField(verbose_name="Description", null=True, blank= True)
    img = models.ImageField(verbose_name="Cover Photo", upload_to ="post_pics/")

    def __str__(self):
        return self.heading

    
  
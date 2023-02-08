from django.db import models
from account.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/category')

    def __str__(self):
        return self.title

class Post(models.Model):
    auther = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ManyToManyField(to=Category)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=70)
    slug = models.SlugField(unique=True, default='')
    thumbnail = models.ImageField(upload_to='blog/blog')
    view = models.IntegerField(default=0)
    upload_date = models.DateField(auto_now_add=True)
    content = RichTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.comment[20]}...'

class Reply(models.Model):
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    reply = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.reply[20]}...'

from django.db import models
from datetime import date
from django.core.validators import MinValueValidator


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=2000)
    image_name = models.ImageField(upload_to='authors')
    email_address = models.EmailField(null=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    excerpt = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image_name = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, verbose_name=(
        ""), on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='tags')

    # def __str__(self):
    #     return self.slug

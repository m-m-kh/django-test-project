from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    choices = (
        ('pub', 'published'),
        ('drf', 'draft')
    )
    
    title = models.CharField(max_length=20)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(choices=choices, max_length=3)
    
    # def get_absolute_url(self):
    #     return reverse("posts_view")
    
    
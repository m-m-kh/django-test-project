from django.forms import ModelForm
from . import models

class NewPostForm(ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'text', 'status', 'author']
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy


class SingUp(generic.FormView):
    form_class = UserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('posts_view')
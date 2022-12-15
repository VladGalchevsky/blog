from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titte'] = 'Classic Blog Design'
        return context


def index(request):
    return render(request, 'blog/index.html')


def get_category(request):
    return render(request, 'blog/category.html')


def get_post(request):
    return render(request, 'blog/category.html')

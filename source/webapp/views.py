from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *


class ArticleList(ListView):
    template_name = 'index.html'
    model = Article


class ArticleDetails(DetailView):
    template_name = 'details.html'
    model = Article

    def get_context_data(self, **kwargs):
        article = kwargs.get('object')
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=article).order_by('-created_at')
        print('kwargs:', kwargs)
        print(context['comments'])
        return context






class ArticleCreate(CreateView):
    template_name = 'article_form.html'
    model = Article
    fields = ['title', 'text', 'author']
    success_url = reverse_lazy('main_url')


class ArticleEdit(UpdateView):
    template_name = 'article_form.html'
    model = Article
    fields = ['title', 'text', 'author']
    success_url = reverse_lazy('main_url')


class ArticleDelete(DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('main_url')


class CommentsView(ListView):
    template_name = 'comments.html'
    model = Comment
    ordering = ['-created_at']


class CommentEdit(UpdateView):
    template_name = 'article_form.html'
    model = Comment
    fields = ['article', 'text', 'author']
    success_url = reverse_lazy('comments_url')


class CommentDelete(DeleteView):
    template_name = 'article_form.html'
    model = Comment
    success_url = reverse_lazy('comments_url')


class CommentCreate(CreateView):

    template_name = 'article_form.html'
    model = Comment
    fields = ['article', 'text', 'author']
    success_url = reverse_lazy('comments_url')

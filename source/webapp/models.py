from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория',
                                 related_name='articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_edit', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey('webapp.Article', related_name='comments',
                                on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse('comment_edit', kwargs={'pk':self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_edit', kwargs={'pk':self.pk})
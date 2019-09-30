"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleList.as_view(), name='main_url'),
    path('article/create/', ArticleCreate.as_view(), name='article_create_url'),
    path('article/edit/<int:pk>/', ArticleEdit.as_view(), name='article_edit_url'),
    path('article/delete/<int:pk>/', ArticleDelete.as_view(), name='article_delete_url'),
    path('article/details/<int:pk>/', ArticleDetails.as_view(), name='article_details_url'),
    path('comments/', CommentsView.as_view(), name='comments_url'),
    path('comments/create/', CommentCreate.as_view(), name='comment_create_url'),
    path('comments/edit/<int:pk>/', CommentEdit.as_view(), name='comment_edit_url'),
    path('comments/delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete_url'),
    path('comments/create/<int:pk>/', CommentCreate)
]

from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    ARTICLE_TYPE = (('News', 'News'),
                    ('Ask', 'Ask'),
                    ('Show', 'Show'),
                    ('GN_plus', 'GN_plus'),)
    type = models.CharField(max_length=20, choices=ARTICLE_TYPE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    likes_num = models.PositiveIntegerField(default=0)
    comments_num = models.PositiveIntegerField(default=0)
    alert = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    alert = models.BooleanField(default=False)
    likes_num = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Likes_Rel(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_articles')

class Comment_Likes_Rel(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='like_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_comments')
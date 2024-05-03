from django.contrib import admin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'date_created')
    list_filter = ('title', 'writer', 'date_created')
    search_fields = ('title', 'writer', 'date_created')
    ordering = ('title', 'date_created')

@ admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'writer', 'parent', 'date_created')
    list_filter = ('content', 'writer', 'parent', 'date_created')
    search_fields = ('content', 'writer', 'parent', 'date_created')
    ordering = ('content', 'date_created')
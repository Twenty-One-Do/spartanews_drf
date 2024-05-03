from rest_framework import serializers
from .models import Article
from Article.models import Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = (
            'id',
            'writer',
            'likes_num',
            'comments_num',
            'date_created',
            'last_updated'
        )

class CommentSerializer(serializers.ModelSerializer):

    class Meta():
        model = Comment
        fields = '__all__'
        read_only_fields = (
            'article',
            'writer',
            'likes_num',
            'date_created',
            'last_updated',
        )


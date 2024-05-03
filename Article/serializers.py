from rest_framework import serializers
from Article.models import Comment


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

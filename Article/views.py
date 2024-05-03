from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Article, Comment, Comment_Rel, Comment_Likes_Rel
from .serializers import CommentSerializer


class ArticleListView(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class ArticleDetailView(APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class CommentListView(APIView):

    def get(self, request, pk):
        comments = Comment.objects.filter(article_id=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            article = get_object_or_404(Article, pk=pk)
            serializer.save(article=article, writer=request.user)


class CommentDetailView(APIView):

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)

        if comment.writer == request.user:
            comment.delete()
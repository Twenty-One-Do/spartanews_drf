from django.db.models import F
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Article, Likes_Rel, Comment, Comment_Likes_Rel
from .serializers import ArticleSerializer, CommentSerializer
from .tasks import send_alert


class ArticleListView(APIView):

    def get(self, request):
        query = request.data.get('query')
        if query is None:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(title__icontains=query)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        # JSON으로 입력하는 데이터 받아오기
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailView(APIView):

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        article = get_object_or_404(Article, pk=pk)

        if request.user != article.writer:
            return Response(stats=status.HTTP_401_UNAUTHORIZED)

        serializer = ArticleSerializer(
            article, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        article = get_object_or_404(Article, pk=pk)

        if request.user != article.writer:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        article.delete()
        data = {"delete": f"Article({pk}) is deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)

class CommentListView(APIView):

    def get(self, request, pk):
        comments = Comment.objects.filter(article_id=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            parent_comment_id = request.data.get('parent_comment_id')
            article = get_object_or_404(Article, pk=pk)

            if parent_comment_id:
                comment = get_object_or_404(Comment, pk=parent_comment_id)
            else:
                comment = None

            registered_comment = serializer.save(
                article=article, writer=request.user, parent=comment)

            if parent_comment_id:
                send_alert.delay(comment.content,
                                comment.writer.email,
                                registered_comment.writer.username,
                                registered_comment.content)
            else:
                send_alert.delay(article.title,
                                article.writer.email,
                                registered_comment.writer.username,
                                registered_comment.content)


            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(
            comment, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)

        if comment.writer == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def article_likes(request, pk):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    article = get_object_or_404(Article, pk=pk)
    ar_rel, create = Likes_Rel.objects.get_or_create(article=article, user=request.user)

    if create:
        article.likes_num = F('likes_num') + 1
    else:
        article.likes_num = F('likes_num') - 1
        ar_rel.delete()

    article.save()
    article.refresh_from_db()

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def comment_likes(request, pk):

    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    comment = get_object_or_404(Comment, pk=pk)
    co_rel, create = Comment_Likes_Rel.objects.get_or_create(
        comment=comment, user=request.user)

    if create:
        comment.likes_num = F('likes_num') + 1
    else:
        comment.likes_num = F('likes_num') - 1
        co_rel.delete()

    comment.save()
    comment.refresh_from_db()

    return Response(status=status.HTTP_200_OK)

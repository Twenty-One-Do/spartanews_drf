from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status

class ArticleListView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        #JSON으로 입력하는 데이터 받아오기
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleDetailView(APIView):

    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        data = {"delete": f"Article({pk}) is deleted."}
        return Response(data, status=status.HTTP_201_CREATED)

class CommentListView(APIView):

    def get(self, request, pk):
        pass

    def post(self, request, pk):
        pass


class CommentDetailView(APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
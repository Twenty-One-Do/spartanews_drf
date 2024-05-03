from rest_framework.views import APIView

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
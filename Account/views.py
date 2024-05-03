from rest_framework.views import APIView
from rest_framework.decorators import api_view


class AccountView(APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

@api_view(['POST'])
def signup(request):
    pass

@api_view(['PUT'])
def change_password(request, pk):
    pass
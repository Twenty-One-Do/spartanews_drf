from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from Account.serializers import UserSerializer


class AccountView(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request, pk):

        if request.user.id != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk):

        if request.user.id != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def change_password(request, pk):

    if not request.user.is_authenticated or request.user.id != pk:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    original_password = request.data.get('original_password')
    new_password = request.data.get('new_password')
    new_password2 = request.data.get('new_password2')
    user = request.user

    if not user.check_password(original_password):
        return Response(
            {
                'error': 'Invalid password',
            },
            status=status.HTTP_403_FORBIDDEN
        )

    if new_password != new_password2:
        return Response(
            {
                'new_password': 'passwords do not match',
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    user.set_password(new_password)
    user.save()
    return Response(status=status.HTTP_200_OK)
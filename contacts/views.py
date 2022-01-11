from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework. permissions import IsAuthenticated
# Create your views here.


class UserApiView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "User Created",
                        'user': serializer.data,
                        'status': status.HTTP_201_CREATED}
            return Response(response)
        else:
            response = {"message": "Error!!!!",
                        'error': serializer.errors,
                        'status': status.HTTP_400_BAD_REQUEST}
            return Response(response)

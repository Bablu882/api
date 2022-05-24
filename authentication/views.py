
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . import serializers




# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"massage":"HelloAuth"},status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer

    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
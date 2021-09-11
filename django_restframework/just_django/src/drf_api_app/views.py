from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.serializers import Serializer

# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

# inherit  testView from apiview
class TestView(APIView):

    # permission_classes = (IsAuthenticated,)


    # method for get request
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        # post_data1 = post_data.first()
        # serializer = PostSerializer(post_data1)
        serializer = PostSerializer(post_data, many=True)
        return Response(serializer.data)

    # method for post request
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




# # Create your views here.
# def test_view(request):
    # data = {
    #     "name" : "Mohammad Asif",
    #     "age" : 20
    # } 
#     return JsonResponse(data)

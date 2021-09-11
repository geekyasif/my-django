# from django.db import models
# from rest_framework import fields, serializers

# from .models import Post

# # This is how we creating froms in django

# # class PostForm(froms.ModelForm):
# #     class Meta:
# #         models = Post
# #         fields = {
# #             'title','description'
# #         }



# # creating serializer is same as form 
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('title', 'description','author')


from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description',
            'author'
        )
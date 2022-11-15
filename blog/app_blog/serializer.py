from rest_framework import serializers 
from app_blog.models import Diabetes,chat

class CustomerSerializers(serializers.ModelSerializer): 
    class meta: 
        model= Diabetes
        fields='__all__'

class CustomerSerializersChat(serializers.ModelSerializer):
    class meta:
        model = chat
        fields = ('comments',)
    
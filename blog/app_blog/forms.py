from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from app_blog.models import Comment, Blog , Diabetes, chat

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class DiabetesForm(forms.ModelForm):
    class Meta:
        model = Diabetes
        fields = '__all__'
        
class ChatForm(forms.ModelForm):
    class Meta:
        model = chat
        fields = '__all__'
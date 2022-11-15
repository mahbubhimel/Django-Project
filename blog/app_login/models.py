from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#related_name field is mainly used to access particular data field directly from a table without using QUERY
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile',on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='user_pics/')

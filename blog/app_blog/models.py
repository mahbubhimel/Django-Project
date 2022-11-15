
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, related_name='post_author')
    blog_title=models.CharField(max_length=256,verbose_name='Put A Title')
    slug = models.SlugField(max_length=264, unique=True)
    blog_content=models.TextField(verbose_name='Write Your Content')
    image=models.ImageField(verbose_name='image',upload_to='post_pics')
    first_post_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_name')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='commenter_name')
    comment = models.TextField(verbose_name='Write Your Comment')
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='liked_user')

    def __str__(self):
        return self.user+ "Likes " +self.blog

class Inference(models.Model):
    name= models.CharField(max_length=255)
    result= models.CharField(max_length=255)
    
    def __str__(self):
        return '{name} => result : {result}'.format(name=self.name,result=self.result)

#     # Coloumns= ["Pregnancies
# Glucose
# BloodPressure
# SkinThickness
# Insulin
# BMI
# DiabetesPedigreeFunction
# Age
# Outcome"]

class Diabetes(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.FloatField(default=0.0)
    DiabetesPedigreeFunction = models.FloatField(default=0.0)
    Age = models.IntegerField()
    # Outcome = This would be predicted by ML model
    
    
class chat(models.Model):
    message = models.CharField(max_length=256)
   
    



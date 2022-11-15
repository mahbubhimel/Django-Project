from django.contrib import admin
from app_blog.models import Blog,Comment, Likes, Diabetes


# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Diabetes)

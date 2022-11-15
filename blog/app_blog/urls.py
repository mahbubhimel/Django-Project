from django.urls import path
from app_blog import views

app_name='app_blog'

urlpatterns=[
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/',views.CreateBlog.as_view(),name='create_blog'),
    path('blog_details/<str:slug>',views.blog_details,name='blog_details'),
    path('my_predictions/',views.prediction_form, name='my_predictions'),



]
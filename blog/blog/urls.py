"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


# the array name of urlpatterns and the apps.urls.py files array name of urlpattern have to be same
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls',namespace='app_login')),
    path('blog/',include('app_blog.urls',namespace='app_blog')),
    path('',views.Index, name='index'),
    

]



# To Add Media files, or upload media files to a direction, below two lines must be added
urlpatterns=urlpatterns+staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
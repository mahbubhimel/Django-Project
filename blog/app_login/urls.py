from django.urls import path
from app_login import views

app_name='app_login'

urlpatterns=[
    path('signup_form/',views.signup_form, name='signup_form' ),
    path('login_page/',views.login_page, name='login_page' ),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('User_profile/',views.User_profile,name='User_profile'),
    path('user_change/',views.user_change,name='user_change'),
    path('profile_pics/',views.profile_pics,name='profile_pics'),
    path('change_profile_pics/',views.change_profile_pics,name='change_profile_pics'),

    
]

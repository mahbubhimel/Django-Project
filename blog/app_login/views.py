from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from app_login.forms import Signup_form, User_change, profile_pic

# Create your views here.
def signup_form(request):
    forms=Signup_form()
    registered = False
    if request.method == 'POST':
        forms = Signup_form(data=request.POST)
        if forms.is_valid():
            forms.save(commit=True)
            registered = True
    diction={'forms':forms, 'registered':registered}
    return render(request, 'app_login/signup.html',context=diction)

def login_page(request):
    forms= AuthenticationForm()
    if request.method=='POST':
        forms = AuthenticationForm(data=request.POST)

        if forms.is_valid():
            username= forms.cleaned_data.get('username') # if form is noT Valid, YOU cannot get cleaned data
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    diction={'forms':forms}
    return render(request,'app_login/login.html',context=diction)

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def User_profile(request):
    return render(request, 'app_login/user_profile.html',context={})


@login_required
def user_change(request):
    current_user = request.user
    form= User_change(instance=current_user) # To get the info of Current Info of the USer
    if request.method== 'POST':
        form = User_change(request.POST, instance=current_user) #(value which will be used, value which will be changed)
        if form.is_valid():
            form.save()
            form = User_change(instance=current_user) # To Showed the latest Changed Value of User
    return render(request,'app_login/user_change.html',context={'form':form})

@login_required
def profile_pics(request):
    forms= profile_pic()
    if request.method=='POST':
        forms=profile_pic(request.POST,request.FILES) # while uploading file, request.FILES has to be added
        if forms.is_valid():
            user_obj = forms.save(commit=False)
            user_obj.user =request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:User_profile'))
            # reverse(app_name: 'name' of the html page which is given in urls.py)

    return render(request, 'app_login/profile_pics.html',context={'forms':forms})

@login_required
def change_profile_pics(request):
    forms=profile_pic(instance=request.user.user_profile)
    if request.method=='POST':
        forms=profile_pic(request.POST,request.FILES,instance=request.user.user_profile ) # while uploading file, request.FILES has to be added
        if forms.is_valid():
            user_obj = forms.save(commit=False)
            user_obj.user =request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:User_profile'))
            # reverse(app_name: 'name' of the html page which is given in urls.py)
    return render(request, 'app_login/profile_pics.html',context={'forms':forms})
    
        
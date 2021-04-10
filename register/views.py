from django.shortcuts import render
from .forms import RegisterForm,UserProfileChange,PasswordChangeForm,ProfilePic,Profiles
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect,reverse,redirect
from django.contrib.auth import logout
from bookworms import views
from register.models import UserProfile



# Create your views here.
def register(response):
    registered=False
    if response.method=="POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            registered=True

    else:
        form=RegisterForm()

    return render(response,"register/signup.html",{"form":form,"registered":registered})



@login_required
def profile(request):
    return render(request,'register/profile.html')

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

@login_required
def user_change(request):
    current_user=request.user
    form=UserProfileChange(instance=current_user)
    profile_form=Profiles(instance=request.user.user_profile)
    if request.method == "POST":
        form=UserProfileChange(request.POST,instance=current_user)
        profile_form=Profiles(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid() and profile_form.is_valid():
            user_form=form.save()
            form2=profile_form.save(commit=False)
            form2.user=user_form
            form2.save()
            return redirect('/profile')


    return render(request,'register/edit_profile.html',context={'form':form,'profile_form':profile_form})

@login_required
def pass_change(request):
    current_user=request.user
    changed=False
    form= PasswordChangeForm(current_user)
    if request.method== "POST":
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True

    return render(request,'register/change_password.html',context={'form':form,'changed':changed})



@login_required
def add_pro_pic(request):
    form=ProfilePic()
    if request.method=="POST":
        form=ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return redirect('/profile')


    return render(request,'register/add_pro_pic.html',context={'form':form})



@login_required

def change_pro_pic(request):
    form=ProfilePic(instance=request.user.user_profile)
    if request.method=="POST":
        form=ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    return render(request,'register/change_pro_pic.html',context={'form':form})

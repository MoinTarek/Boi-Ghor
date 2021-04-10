from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from register.models import UserProfile


class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]



def save(self,commit=True):
    user=Super(RegisterForm,self).save(commit=False)
    user.first_name= cleaned_data('first_name')
    user.last_name=cleaned_data('last_name')
    user.email=cleaned_data('email')


    if commit:
        user.save()

    return user




class UserProfileChange(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]



class ProfilePic(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=['profile_pic']




class Profiles(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=['age','location','phone']

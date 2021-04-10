from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    age=models.IntegerField(null=True,blank=True,default=0)
    location= models.CharField(max_length=100,null=True,blank=True,default="")
    phone=models.IntegerField(null=True,blank=True,default=0)
    profile_pic=models.ImageField(upload_to='profile_pics')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)

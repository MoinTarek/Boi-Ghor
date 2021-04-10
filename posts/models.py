from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,default="",related_name='post_author')
    title= models.CharField(max_length=240)
    post_type=(
    ('Sale',"Sale"),
    ('Rent',"Rent"),
    ('Exchange',"Exchange"),

    )
    type= models.CharField(max_length=200,choices=post_type)
    description = models.CharField(blank=True,null=True,max_length=400)
    price= models.IntegerField(blank=True,null=True)
    summary= models.TextField(blank=True,null=True)
    address= models.CharField(blank=True,null=True,max_length=400)
    condition=models.CharField(blank=True,null=True,max_length=200)
    period= models.IntegerField(blank=True,null=True)
    interest=models.CharField(blank=True,null=True,max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    post_image=models.ImageField(upload_to='post_images',null=True,blank=True)




    def get_absolute_url(self):
        return f"post/{self.id}"


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-comment_date',)


    def __str__(self):
        return self.comment

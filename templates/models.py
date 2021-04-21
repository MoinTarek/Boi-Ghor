from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_post_author')
    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(verbose_name="What is on your mind?")
    blog_image=models.ImageField(upload_to='blog_images',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.blog_title



class BlogComment(models.Model):
    blog_post=models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='blog_post_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_user_comment')
    blog_comment=models.TextField()
    blog_comment_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-blog_comment_date',)


    def __str__(self):
        return self.blog_comment




class Likes(models.Model):
    blog=models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='liked_blog')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked_user')



    def __str__(self):
        return self.user+ " likes " + self.blog

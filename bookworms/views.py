from django.shortcuts import render
from django.http import HttpResponse
from posts.views import post_create_view,dynamic_lookup_view
from posts.models import Post

def home(response):
    obj=Post.objects.all().order_by('-id')
    context={
            'obj':obj
            }
    return render(response,"bookworms/homepage.html",context)



def used_books(response):
    return render(response,"bookworms/used_books.html")



def shopx(response):
    return render(response,"bookworms/shop.html")


def arts(response):
    return render(response,"bookworms/arts.html")

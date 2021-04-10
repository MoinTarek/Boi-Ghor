from django.shortcuts import render,get_object_or_404
from .forms import PostCreateForm,CommentForm
# Create your views here.
from django.shortcuts import HttpResponseRedirect,reverse,redirect
from django.urls import reverse_lazy
from .models import Post,Comment
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView





def post_create_view(request):
    form = PostCreateForm()
    if request.method=="POST":
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("/")

    return render(request,"posts/createpost.html",context={'form':form})




def dynamic_lookup_view(request,id):
    post=Post.objects.get(id=id)
    comment_form=CommentForm()
    context={
            'comment_form':comment_form,
            'post':post

        }

    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
            comment.post=post
            comment.comment_date=timezone.now()
            comment.save()
            return HttpResponseRedirect(reverse('Posts:post',kwargs={'id':id}))



    return render(request,"posts/post_detail.html",context)



def postview(request):
    allPosts=Post.objects.all()
    context={
            'title': obj.title,
            'description': obj.description,
            'type': obj.type,
            'price': obj.price,
            'summary': obj.summary,
            'address': obj.address,
            'condition': obj.condition,
            'period': obj.period,
            'interest': obj.interest,
            'post_image':obj.post_image
    }
    return render(request,"bookworms/homepage.html",context)


def MyPosts(response):
    return render(response,"posts/user_posts.html")

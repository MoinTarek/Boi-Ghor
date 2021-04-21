from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.shortcuts import HttpResponseRedirect,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import BlogPost,BlogComment,Likes
from .forms import BlogCommentForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,CreateView,UpdateView,ListView,DetailView,View,TemplateView,DeleteView
import uuid




class CreateBlog(LoginRequiredMixin,CreateView):
    model=BlogPost
    template_name='blog/create_blog.html'
    fields = ('blog_title','content','status')


    def form_valid(self,form):
        blog_obj=form.save(commit=False)
        blog_obj.author=self.request.user
        title=blog_obj.blog_title
        blog_obj.slug=title.replace(" ","-") + "-"+str(uuid.uuid4())
        blog_obj.save()
        return redirect("/blog/")
        #return HttpResponseRedirect(reverse('blog_list'))




class BlogList(ListView):
    context_object_name='blogs'
    model=BlogPost
    template_name='blog/blog_home.html'






def Blog_Details(request,slug):
    blog=BlogPost.objects.get(slug=slug)
    comment_form=BlogCommentForm()
    already_liked=Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked= True
    else:
        liked=False

    if request.method=="POST":
        comment_form=BlogCommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
            comment.blog_post=blog
            comment.comment_date=timezone.now()
            comment.save()
            return HttpResponseRedirect(reverse('blog:blog_detail',kwargs={'slug':slug}))

    return render(request,'blog/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})




@login_required
def liked(request,pk):
    blog=BlogPost.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=user)

    if not already_liked:
        liked_post=Likes(blog=blog,user=user)
        liked_post.save()
        return HttpResponseRedirect(reverse('blog:blog_detail',kwargs={'slug':blog.slug}))


@login_required
def unliked(request,pk):
    blog=BlogPost.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog:blog_detail',kwargs={'slug':blog.slug}))

from . import views
from django.urls import path

app_name='blog'

urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog_list'),
    path('blog/write/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog/details/<slug:slug>', views.Blog_Details, name='blog_detail'),
    path('blog/liked/<pk>/', views.liked, name='liked_post'),
    path('blog/unliked/<pk>/', views.unliked, name='unliked_post'),
]

from django.urls import path

from . import views

app_name='Posts'

urlpatterns= [
path("post/<int:id>",views.dynamic_lookup_view,name="post"),
path("createpost/",views.post_create_view,name="create_post"),
path("my_posts/",views.MyPosts,name="my_posts"),

]

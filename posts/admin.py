from django.contrib import admin
from posts.models import Post,Comment
# Register your models here.
from .models import Post

admin.site.register(Post)
admin.site.register(Comment)

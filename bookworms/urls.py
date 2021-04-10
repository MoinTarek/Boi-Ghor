from django.urls import path

from . import views


urlpatterns= [
path("",views.home,name="home"),
path("used/",views.used_books,name="used_books"),
path("shopx/",views.shopx,name="shopx"),
path("arts/",views.arts,name="arts"),

]

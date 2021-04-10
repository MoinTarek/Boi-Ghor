from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns


urlpatterns = [
    path("register/",views.register,name="register" ),
    path("profile/",views.profile,name="profile" ),
    path("login/",auth_views.LoginView.as_view(template_name="register/login.html"),name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("edit_profile/", views.user_change, name="edit_profile"),
    path("pass_change/", views.pass_change, name="pass_change"),
    path("profile_picture/", views.add_pro_pic, name="add_pro_pic"),
    path("change_profile_picture/", views.change_pro_pic, name="change_pro_pic"),
]

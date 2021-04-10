
from django.contrib import admin
from django.urls import path
from bookworms import views
from django.urls import include, path
from register import views
from posts import views
from blog import views
from chat import views
from contact import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns



urlpatterns = [
    path('',include("bookworms.urls")),
    path('',include("chat.urls")),
    path('',include("register.urls")),
    path('',include("posts.urls")),
    path('',include("blog.urls")),
    path('admin/', admin.site.urls),
    path("",include("django.contrib.auth.urls")),
    path('', include('App_Shop.urls')),
    path('shop/', include('App_Order.urls')),
    path('payment/', include('App_Payment.urls')),
     path('',include("contact.urls")),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

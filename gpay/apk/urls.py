from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indx,name='index'),
    path('index/', views.indx,name='index'),
    path('register/', views.cregister,name='cregister'),
    path('login/', views.clogin,name='clogin'),
    path('home/', views.home,name='home'),
    path('logout/', views.logout,name='logout'),
   
   
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
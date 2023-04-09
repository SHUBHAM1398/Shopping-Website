from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path("home",views.index,name="home"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact")
]
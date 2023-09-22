from django.contrib import admin
from django.urls import include, path
from . import views

# Add all file diroctery in side the view and templet filename as acdording to the views. py
# Create a templets filefor html 
# Create a static file for img,css,js



urlpatterns = [
   path('',views.home,name="home"),
   path('signup',views.signup,name="signup"),
   path('signout',views.signout,name="signout"),
   path('signin',views.signin,name="signin"),
   path('about',views.about,name="about"),
   path('contact',views.contact,name="contact"),
   path('design',views.design,name="design"),
   path('preatics',views.preatics,name="preatics"),
   path('userdetails',views.userdetails,name="userdetails"),
   path('regst',views.regst,name="regst"),
   path('u_dash',views.u_dash,name="u_dash"),
   #path('',views.,name=""),
]

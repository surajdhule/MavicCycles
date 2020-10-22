from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.registrationPage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('home/', views.homepage, name='home'),
]

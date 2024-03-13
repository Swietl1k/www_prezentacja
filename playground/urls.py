from django.urls import path
from . import views

#URL Configuration module
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello2/', views.say_hello2),
    path('all_users/', views.view_users),
    path('all_users/users_details/<slug:slug>', views.view_details),
    path('testing/', views.view_testing),
]
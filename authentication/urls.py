from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('addPreference/', views.addPreference, name='addPreference'),
    path('addSubscription/', views.addSubscription, name='addSubscription'),
    path('createSubscription/', views.createSubscription, name='createSubscription'),
    path('sendMessage/', views.sendMessage, name='sendMessage')
]
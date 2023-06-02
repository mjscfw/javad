

from django.contrib import admin
from django.urls import path,include
from .views import LoginView, pending

urlpatterns = [
    path('', LoginView.as_view(), name = 'home'),
    path('pending', pending, name='pending')
]

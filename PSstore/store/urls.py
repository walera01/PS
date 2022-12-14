from django.urls import path, include
from store.views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('login', logout, name='logout'),
    path('test', test),
]
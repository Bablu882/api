from unicodedata import name
from django.urls import path
from . import views


urlpatterns=[
    path('hello_auth',views.HelloAuthView.as_view(),name='hello_auth'),
    path('signup',views.UserCreateView.as_view(),name='signup'),
]
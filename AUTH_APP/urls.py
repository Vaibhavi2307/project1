from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',Signup_view.as_view(),name='signup_url'),
    path('signin/',Login_view.as_view(),name='signin_url'),
    path('signout/',Delete_view.as_view(),name='signout_url')
]
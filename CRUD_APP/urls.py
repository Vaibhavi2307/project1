from django.urls import path
from.views import *


urlpatterns=[
    path('employee/',Employee_view.as_view(),name='employee_url'),
    path('show/',Show_view.as_view(),name='show_url'),
    path('update/<int:pk>/',Update_view.as_view(),name='update_url'),
    path('delete/<int:pk>/',Delete_view.as_view(),name='delete_url')
]
from django.urls import path
from .views import *
urlpatterns = [
    path('createstudent/',StudentCreateAPIView.as_view()),
    path('',StudentAPIView.as_view()),
]







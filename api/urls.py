from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
path("" ,  Dataviewcreate_api.as_view()),
path("<int:pk>/" , DataUpdaeDelete.as_view())
]

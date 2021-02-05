
from django.urls import path,include
from . import views

urlpatterns = [
    path('ass1',views.assignment1,name="ass1"),
    path('ass2',views.assignment2,name="ass2"),
    path('ass3',views.assignment3,name="ass3"),
    path('ass4',views.assignment4,name="ass4"),
    path('ass5',views.assignment5,name="ass5"),
    path('ass6',views.assignment6,name="ass6"),
    path('fb',views.fb,name="fb"),
    path('ass7',views.assignment7,name="ass7")
]

from django.urls import path,include
from . import views

urlpatterns = [
    path('ass1',views.assignment1,name="ass1"),
    path('ass2',views.assignment2,name="ass2"),
    path('ass3',views.assignment3,name="ass3"),
    path('ass4',views.assignment4,name="ass4"),
    path('form',views.form,name="form")
]
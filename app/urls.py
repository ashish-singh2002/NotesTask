from django.urls import path,include
from. import views

urlpatterns = [
    path('',views.insert,name="insert"),
    path('read',views.read,name="read"),
    path('<int:id>/edit/',views.edit,name="edit"),
    path('<int:id>/delete/',views.delete,name="delete"),
   
]

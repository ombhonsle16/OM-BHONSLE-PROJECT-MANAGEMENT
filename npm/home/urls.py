from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ),
    path('contactus/',views.contactUs),
    path('contactsubmit/',views.contactSubmit),
]

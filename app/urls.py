from django.urls import path
from .views import *
urlpatterns = [
#   path('',index),
    path('', Home.as_view()),
    path('about',About.as_view()),
    path('contact',Contact.as_view()),
]

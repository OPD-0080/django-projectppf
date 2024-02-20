from django.urls import path, include

## IMPORTATION OF CUSTOM MODULES
from . import post
    
urlpatterns = [
    path('register/', post.register, name="register"),
    
    
    
]

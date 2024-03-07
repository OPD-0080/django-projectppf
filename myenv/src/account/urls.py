from django.urls import path, include

## IMPORTATION OF CUSTOM MODULES
from . import post
from . import views
urlpatterns = [
    path('register/', post.register, name="register"),
    path('signup/', post.signup, name="signup"),
    path('otpverification/', post.otp_verification, name="otp_verification"),
    
    
    path('signup/', views.signup, name="view_signup"),
    path('registration/', views.registration, name="view_registration"),
    path('404/', views.page_not_found, name="view_404"),
    path('500/', views.internal_server_error, name="view_500"),
]

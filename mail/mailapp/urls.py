from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('email_verified/', views.email_verified, name='email_verified'),
]
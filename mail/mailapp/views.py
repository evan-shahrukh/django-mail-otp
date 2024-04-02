from django.shortcuts import render, redirect
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string

def register(request):
    register_dict = {"title" : "Registration"}
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.create_user(email=email)
        otp = get_random_string(length=6, allowed_chars='0123456789')
        request.session['otp'] = otp
        send_mail('OTP Verification', f'Your OTP is: {otp}', settings.EMAIL_HOST_USER, [email])
        return redirect('verify_otp')
    return render(request, 'registration.html',context=register_dict)

def verify_otp(request):
    verify_dict = {"title" : "Email Verification"}
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == request.session.get('otp'):
            del request.session['otp']
            return redirect('email_verified')
        else:
            verify_dict.update({"not_verified" : True})
            return render(request, 'verify_otp.html', context=verify_dict)
    return render(request, 'verify_otp.html', context=verify_dict)

def email_verified(request):
    verified_dict = {"title" : "Email Verified"}
    return render(request, "email_verified.html", context=verified_dict)
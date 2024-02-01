
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from .forms import UserRegistrationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from .decorators import unauthenticated_user, judge_required
from django.contrib.auth.hashers import make_password
import random

@csrf_exempt
def VerifyOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 == password2:
            hashed_password = make_password(password1)
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                is_judge = True,
            )
    return JsonResponse({'data' : 'success'}, status = 200)

def home(request):
    return render(request, 'customUser/mainpage.html')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            otp = str(random.randint(100000, 999999))
            # send_mail('OTP for registration', otp, 'abhinav25102005@gmail.com', [form.cleaned_data['email']], fail_silently=False)
            print(otp)
            return render(request, 'customUser/verify.html', {'otp' : otp, 'username':username, 'first_name':first_name, 'last_name':last_name, 'email':email, 'password1':password1, 'password2':password2})
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'customUser/register.html', context)

def redirectuser(request):
    return redirect('/login/')
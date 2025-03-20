from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, ForgotPasswordForm
from .models import User
from django.contrib.auth import authenticate, login as auth_login, logout

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"]) 
            user.is_active = True  # নিশ্চিত করুন ইউজার অ্যাক্টিভ
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             try:
#                 user = User.objects.get(email=email, password=password)
#                 messages.success(request, "Login successful!")
#                 return redirect('shop:product_list')  # Redirect to a home page
#             except User.DoesNotExist:
#                 messages.error(request, "Invalid email or password")
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login successful!")
                return redirect('shop:product_list')
            else:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.success(request, "Password reset link sent to your email!")
            else:
                messages.error(request, "Email not found")
    else:
        form = ForgotPasswordForm()
    return render(request, 'registration/forgot_password.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('accounts:login')

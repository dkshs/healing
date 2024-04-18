from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from healing.utils.validate import validate

MIN_PASSWORD_LENGTH = 8


def sign_up(request):  # noqa: PLR0911
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username") or ""
        email = request.POST.get("email") or ""
        password = request.POST.get("password") or ""
        confirm_password = request.POST.get("confirm_password") or ""
        if not validate([username, email, password, confirm_password]):
            messages.error(request, "Please fill in all fields")
            return redirect("sign_up")
        if len(password.strip()) < MIN_PASSWORD_LENGTH:
            messages.error(
                request,
                f"Password must be at least {MIN_PASSWORD_LENGTH} characters",
            )
            return redirect("sign_up")
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("sign_up")
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect("sign_up")
        if " " in password:
            messages.error(request, "Password cannot contain spaces")
            return redirect("sign_up")
        try:
            user = User.objects.create_user(username, email=email, password=password)
            messages.success(request, "User created successfully")
            login(request, user)
            return redirect("home")
        except Exception as e:  # noqa: BLE001
            messages.error(request, f"Error creating user: {e}")
            return redirect("sign_up")
    return render(request, "sign_up.html")


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username") or ""
        password = request.POST.get("password") or ""
        if not validate([username, password]):
            messages.error(request, "Please fill in all fields")
            return redirect("sign_in")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        messages.error(request, "Invalid username or password")
        return redirect("sign_in")
    return render(request, "sign_in.html")


def sign_out(request):
    logout(request)
    return redirect("sign_in")

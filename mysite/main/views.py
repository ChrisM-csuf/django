from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .hangman import hangman

# Create your views here.
def homepage(request):
    return render(request=request,
    template_name="main/home.html",
    context={"tutorials": Tutorial.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.data['password1'])
        print(form.data['password2'])
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created!: {username}")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")



    form = RegistrationForm
    return render(request, "main/register.html", context={"form": form})

def login(request):
    if request.method == "POST":
        print(form.data['username'])
        print(form.data['password'])
    else:
        print("Oh no")

    login_form = LoginForm
    return render(request=request,
    template_name="main/login.html")

def ranches(request):
    return render(request=request,
    template_name="main/ranches.html")

def game(request):
    hangman()
    return render(request=request,
    template_name="main/game.html")

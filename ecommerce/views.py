from django.http import request
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login

from .forms import ContactForm, RegisterForm, LoginForm


def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title": "Hello World!",
        "content": " Welcome to the homepage.",

    }
    if request.user.is_authenticated():
        context["premium_content"] = "yep"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": " Welcome to the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": " Welcome to the contact page.",
        "form": contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    if request.method == "POST":
        # print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):

    return render(request, "auth/login.html", {})


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    ctx = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", ctx)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):

    context = {
        'page_title' : 'Home'
    }
    return render(request, 'index.html', context)

def loginView(request):

    context = {
        'page_title': 'LOGIN'
    }
    user = None

    if request.method == 'POST':
        print(request.POST)
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password = password_login)
        print(user)
        if user is not None:

            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html', context)


def logoutView(request):

    context = {
        'page_title' : 'logout'
    }

    if request.method == "POST":
        print(request.POST)
        if request.POST["logout"] == "Submit":
            logout(request)

            return redirect('index')
        print(" proses logout")

    return render(request, 'logout.html', context)


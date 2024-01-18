from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        # subscriptions = request.POST('subscriptions')
        # preferences = request.POST('preferences')

        myUser = User.objects.create_user(userName, email, password)
        myUser.first_name = firstName
        myUser.last_name = lastName
        
        myUser.save()
        messages.success(request, "User created successfully")

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']

        user = authenticate(username=userName, password=password)
        
        if user is None:
            messages.error(request, "User not found")
            return redirect('signin')

        if user is not None:
            login(request, user)
            messages.success(request, "Sign in successful")
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Sign out successful")
    return redirect('home')
from django.shortcuts import redirect, render
from django.http import HttpResponse
from authentication.models import User  # Import the correct User model
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login, logout
from authentication.models import Subscription

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
        userType = request.POST['userType']
        print(userType)
        # subscriptions = request.POST('subscriptions')
        # preferences = request.POST('preferences')

        myUser = User.objects.create_user(userName, email, password)
        myUser.first_name = firstName
        myUser.last_name = lastName
        myUser.type = userType
        
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

def addPreference(request):
    if request.method == 'POST':
        preferences = request.POST.getlist('preference')  # Get the preference array from the request
        myUser = request.user  # Assuming the authenticated user is accessing this function
        myUser.preferences = preferences
        myUser.save()

        messages.success(request, "Preferences added successfully")

        return redirect('home')

    return render(request, 'authentication/add_preference.html')

def addSubscription(request):
    if request.method == 'POST':
        subscription_id = request.POST['subscription_id']
        myUser = request.user
        try:
            subscription = Subscription.objects.get(id=subscription_id)
            myUser.subscription.add(subscription)
            myUser.save()
            messages.success(request, "Subscription added successfully")
        except Subscription.DoesNotExist:
            messages.error(request, "Subscription not found")
        return redirect('home')

    return render(request, 'authentication/add_subscription.html')

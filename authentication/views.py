from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from authentication.models import User  # Import the correct User model
import django.contrib.messages as messages
from django.contrib.auth import authenticate, login, logout
from authentication.models import Subscription, Alert
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

def home(request):
    if request.user.is_authenticated:
        fname = request.user.first_name
        if request.user.type == 'admin':
            return render(request, 'authentication/adminDashboard.html', {'fname': fname})
        else:
            return render(request, 'authentication/userDashboard.html', {'fname': fname})
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
            if user.type == 'admin':
                return render(request, 'authentication/adminDashboard.html', {'fname': fname})
            else:
                return render(request, 'authentication/userDashboard.html', {'fname': fname})

    return render(request, 'authentication/signin.html')

@login_required
def signout(request):
    logout(request)
    messages.success(request, "Sign out successful")
    return redirect('home')

@login_required
def addPreference(request):
    if request.method == 'POST':
        preferences = request.POST.getlist('preference')  # Get the preference array from the request
        myUser = request.user  # Assuming the authenticated user is accessing this function
        myUser.preferences = preferences
        myUser.save()

        messages.success(request, "Preferences added successfully")

        return redirect('home')

    return render(request, 'authentication/add_preference.html')

@login_required
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

@login_required
def createSubscription(request):
    if request.method == 'POST':
        orgName = request.POST.get('orgName')
        subscriptionName = request.POST.get('subscriptionName')
        print(orgName)
        print(subscriptionName)

        # Create the subscription
        new_subscription = Subscription.objects.create(name=subscriptionName, org=orgName)
        print(new_subscription)
        # Associate the new subscription with the current user
        request.user.subscription.add(new_subscription)
        request.user.save()

        # Optionally, you can use messages.success for user feedback
        messages.success(request, 'Subscription created successfully.')

        return redirect('home')

    return render(request, 'authentication/createSubscription.html')

@login_required
def editSubscription(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)

    if request.method == 'POST':
        subscription_name = request.POST.get('subscriptionName')
        org_name = request.POST.get('orgName')

        if subscription_name:
            subscription.name = subscription_name
        if org_name:
            subscription.org = org_name

        subscription.save()
        messages.success(request, "Subscription edited successfully")
        return redirect('home')

    return render(request, 'authentication/editSubscription.html', {'subscription': subscription})

@login_required
def deleteSubscription(request, subscription_id):
    try:
        subscription = Subscription.objects.get(id=subscription_id)
        subscription.delete()
        messages.success(request, "Subscription deleted successfully")
    except Subscription.DoesNotExist:
        messages.error(request, "Subscription not found")
    return redirect('home')

@login_required
def sendMessage(request, subscription_id):
    if request.method == 'POST':
        print(request.user.type)
        if request.user.type == 'admin':
            print(request.POST.get('subscriptionId'))
            subscription_id = request.POST.get('subscriptionId')
            message = request.POST.get('message')
            
            # Get the subscription
            subscription = Subscription.objects.get(id=subscription_id)
            print(subscription)
            # Get users subscribed to the subscription
            users_subscribed = subscription.user_set.all()
            print(users_subscribed)
            if users_subscribed.exists():
                # Create an alert for each user subscribed to the subscription
                for user in users_subscribed:
                    alert = Alert.objects.create(
                        subscription=subscription,
                        message=message,
                        date=now()
                    )
                    alert.users.add(user)
                    print(alert)
                
                messages.success(request, "Message sent successfully")
            else:
                messages.warning(request, "No users subscribed to this subscription")

            return redirect('home')  # Redirect to the home page or wherever you want
        
        messages.error(request, "You do not have permission to send messages")
        return redirect('home')
    
    return render(request, 'authentication/sendMessage.html', {'subscription_id': subscription_id})

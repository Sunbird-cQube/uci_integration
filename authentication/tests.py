from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Subscription, Alert

User = get_user_model()

class AuthenticationViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a test subscription
        self.subscription = Subscription.objects.create(name='Test Subscription', org='Test Org')

        # Login the test user
        self.client = Client()
        self.client.login(username='testuser', password='password')

    def test_home_view_authenticated_user(self):
        # Test home view for authenticated user
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/userDashboard.html')

    def test_home_view_unauthenticated_user(self):
        # Test home view for unauthenticated user
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/index.html')

    def test_signup_view(self):
        # Test signup view
        response = self.client.post(reverse('signup'), {
            'userName': 'newuser',
            'firstName': 'New',
            'lastName': 'User',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'confirmPassword': 'newpassword',
            'userType': 'user'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to signin page upon successful signup

    def test_signin_view(self):
        # Test signin view
        response = self.client.post(reverse('signin'), {
            'userName': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_signout_view(self):
        # Test signout view
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)

    def test_addPreference_view(self):
        # Test addPreference view
        response = self.client.post(reverse('addPreference'), {
            'preference': 'Test Preference'
        })
        self.assertEqual(response.status_code, 302)

    def test_addSubscription_view(self):
        # Test addSubscription view
        response = self.client.post(reverse('addSubscription'), {
            'subscription_id': self.subscription.id
        })
        self.assertEqual(response.status_code, 302)
    
    def test_createSubscription_view(self):
        # Test createSubscription view
        response = self.client.post(reverse('createSubscription'), {
            'subscriptionName': 'TestSubscription',
            'orgName': 'Test Org'
        })
        self.assertEqual(response.status_code, 302)
    
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect

from django.http import JsonResponse
import base64
import hmac
import hashlib
import json
from django.conf import settings

# Define a function to encode the JWT
def base64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

def encode_jwt(header, payload, secret):
    encoded_header = base64url_encode(json.dumps(header).encode('utf-8'))
    encoded_payload = base64url_encode(json.dumps(payload).encode('utf-8'))
    
    message = f'{encoded_header}.{encoded_payload}'
    signature = hmac.new(secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).digest()
    encoded_signature = base64url_encode(signature)
    
    return f'{encoded_header}.{encoded_payload}.{encoded_signature}'

# Define a view function for the home page
def home(request):
    return render(request, 'register.html')

# Define a view function for the login page
def login_view(request):  # Renamed to avoid conflict with the imported login
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user
            auth_login(request, user)
            
            # Create JWT token for the user
            header = {
                "alg": "HS256",
                "typ": "JWT"
            }
            
            payload = {
                "user_id": user.id,
                "username": user.username,
                "role": "admin" if user.is_superuser else "user"
            }
            
            # Generate JWT
            secret = settings.SECRET_KEY
            token = encode_jwt(header, payload, secret)
            
            # Redirect to the React frontend with the token as a query parameter
            react_frontend_url = 'http://localhost:3000'  # Your React app URL
            return HttpResponseRedirect(f'{react_frontend_url}?token={token}')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        if User.objects.filter(username=username).exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    # Render the registration page template (GET request)
    return render(request, 'register.html')

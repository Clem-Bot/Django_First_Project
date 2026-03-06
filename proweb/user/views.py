from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.
def login_users(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            #print('Username does not exist')
            messages.error(request, 'User name does not exist')
        user = authenticate(request, username = username, password = password)
        #if the user exists after filling in the credentials it would direct them to the home page
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            #print('User name or password is incorrect')
            messages.error(request,'user name or password is incorrect')
    return render(request, 'user/login.html')

def logout_users(request):
    logout(request)
    messages.success(request, 'User is successfully logged out')
    return redirect('login_users')

def register_users(request):
    page = 'register'
    #form = UserCreationForm() #This creates an instance of a UserCreationForm
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'you have created an account succesfully')
    context = {'page': page, 'form': form} #passes the form to context for rendering purposes
    return render(request, 'user/login.html', context)

from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import siteViewCounter
from eventApp.models import Event
from attendee.models import Attendee
from .forms import LoginForm , SignupForm
# Create your views here.
def home(request):
    # increment the counter for this route view
    total_views  , created= siteViewCounter.objects.get_or_create(id=1)
    total_views.total_views += 1
    total_views.save()
    try : 
        events = Event.objects.last().id
    except AttributeError:
        events = 0
    try:
        attendees = Attendee.objects.last().id
    except AttributeError:
        attendees = 0
    counts = {'views':total_views.total_views,  
            'events': events,
            'attendees': attendees,
            'users':User.objects.all().count()}
    
    return render(request,'home.html' , {'counts':counts})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        isEmailExist = User.objects.filter(email=request.POST['email']).exists()
        if isEmailExist:
            messages.info(request, 'Email already exists ! Please Login')
            return render(request, 'signup.html', {'form': form})
        if request.POST['password'] != request.POST['confirm_password']:
            messages.info(request, 'Password Mismatch !')
            return render(request, 'signup.html', {'form': form})
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
                
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email).first()
            if not user:
                messages.info(request, 'User does not exist')
                return render(request, 'login.html', {'form': form})
            else:
                username = user.username
                user = auth.authenticate(username=username, password=password)
                if user is None:
                    messages.info(request, 'Password is incorrect')
                    return render(request, 'login.html', {'form': form})
                else:
                    auth.login(request, user)
                    next_url = request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def logout(request):
    auth.logout(request)
    return redirect('home')

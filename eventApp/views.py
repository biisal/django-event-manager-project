from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event
from attendee.models import Attendee
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages
# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        description = json.loads(form.data.get('description'))
        if description.get('html') == '<p>Enter Your Description</p>' or description.get('html') == '<p><br></p>': # ignoring unnecessary blank description
            messages.error(request, 'Enter a valid description')
            return render(request, 'events/create.html', {'form': form})
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event created successfully, view your event : <a href="/view/">View</a>')
            return redirect('create')
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})

@login_required
def view(request):
    user = request.user
    eventCreated = Event.objects.filter(user=user).order_by('-id')
    return render(request, 'events/view.html', {'userEvent': eventCreated})

@login_required
def edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        if request.user == event.user:
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('view')
    else:
        if request.user == event.user:
            form = EventForm(instance=event)
            return render(request, 'events/edit.html', {'form': form, 'id': id})
    return redirect('home')

@login_required
def delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.user == event.user:
        event.delete()
    return redirect('view')

@login_required
def details(request, id):
    
    event = get_object_or_404(Event, id=id)    
    attendee =Attendee.objects.filter(registered_for=event)
    total_registered = attendee.count()
    return render(request, 'events/details.html', {
        'event': event,
        'attendees': attendee,
        'total_registered': total_registered
    })

from django.shortcuts import render , HttpResponse , redirect  , get_object_or_404
# import messages
from django.contrib import messages
from eventApp.models import Event
from .models import Attendee
from django.contrib.auth.decorators import login_required
# show all events expecte by the user
def allevents(request):
    try:
        user = request.user
        events = Event.objects.exclude(user=user).order_by('-id')
        registered_event_ids = Attendee.objects.filter(name=user).values_list('registered_for', flat=True)
    except TypeError:
        events = Event.objects.all()
        registered_event_ids = []
    return render(request, 'attendee/allevants.html', {'events': events , 'registered_event_ids':registered_event_ids})

@login_required
def register(request, id):
    event = get_object_or_404(Event, id=id)
    attendee, created = Attendee.objects.get_or_create(name=request.user, registered_for=event)
    
    if not created:
        messages.error(request, 'You are already registered for the event')
    else:
        attendee.save()
        messages.success(request, 'Successfully Registered for the event')
        
    return redirect(f'/allevents?registered_event_id={event.id}')


    
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration


def event_list(request):
    events = Event.objects.all()

    return render(request, 'registrations/event_list.html', {
        'events': events
    })


def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        Registration.objects.create(
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            event=event
        )

        return redirect('event_list')

    return render(request, 'registrations/register.html', {
        'event': event
    })
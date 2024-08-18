from datetime import datetime

from django.shortcuts import render, get_object_or_404
from online_classes.forms import SessionForm
from online_classes.models import Session


# Create your views here.
def all_sessions(request,name=None):
    # sessions = Session.objects.prefetch_related('participants').all()
    # for session in sessions:
    #     for person in session.participants.all():
    #         print(person.first_name)
    if name == 'start':
        sessions = Session.objects.filter(start_time__gt=datetime.now())
        return render(request, 'home.html', {"sessions": sessions })
    elif name == 'stop':
        sessions = Session.objects.filter(end_time__gt=datetime.now())
        return render(request, 'home.html', {"sessions": sessions})
    else:
        return render(request, 'home.html', {"sessions": Session.objects.all()})


def create_session(request):
    context = dict()

    my_form = SessionForm(request.POST or None)
    context["form"] = my_form

    if request.method == 'POST':
        if my_form.is_valid():
            my_form.save()
            print("Saved!")

    return render(request, "session_form.html", context)


def edit_session(request, pk):
    obj = get_object_or_404(Session, pk=pk)
    # context = {}

    if request.method == "POST":
        my_form = SessionForm(request.POST, instance=obj)
        if my_form.is_valid():
            my_form.save()
            print("Edited! ")

    return render(request, "session_form.html", {"form": SessionForm(instance=obj)})


def detail_session(request, pk):
    obj = get_object_or_404(Session, pk=pk)
    return render(request, "detail_session.html", {"session": obj })

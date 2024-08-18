from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from online_classes.forms import SessionForm
from online_classes.models import Session


# Create your views here.
def all_sessions(request):
    error = None
    if request.method == "POST":
        start_time, end_time = request.POST["start"], request.POST["end"]
        if start_time and end_time and start_time < end_time:
            sessions = Session.objects.filter(end_time__lte=end_time, start_time__gte=start_time)
            return render(request, 'home.html', {"sessions": sessions})
        else:
            error = "please enter valid date "

    return render(request, 'home.html', {"sessions": Session.objects.all(), "error": error})


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
            return redirect("home")
    return render(request, "session_form.html", {"form": SessionForm(instance=obj)})


def detail_session(request, pk):
    obj = get_object_or_404(Session, pk=pk)
    return render(request, "detail_session.html", {"session": obj})


def delete_session(request, pk):
    obj = get_object_or_404(Session, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("home")
    return render(request, "confirm.html", {"session": obj})

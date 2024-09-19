from django.shortcuts import render
from online_classes.models import Session

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


# Create your views here.
# def all_sessions(request):
#     error = None
#     if request.method == "POST":
#
#         if start_time and end_time and start_time < end_time:
#             sessions = Session.objects.filter(end_time__lte=end_time, start_time__gte=start_time)
#             return render(request, 'home.html', {"sessions": sessions})
#         else:
#             error = "please enter valid date "
#
#     return render(request, 'home.html', {"sessions": Session.objects.all(), "error": error})


class AllSessions(ListView):
    model = Session
    template_name = 'home.html'
    context_object_name = 'sessions'

    def post(self, request, *args, **kwargs):
        # context = super().get_queryset()
        start_time, end_time = request.POST["start"], request.POST["end"]
        if start_time and end_time and start_time < end_time:
            sessions =  Session.objects.filter(end_time__lte=end_time, start_time__gte=start_time)
            return render(request, self.template_name, {self.context_object_name: sessions})

        messages.add_message(request, messages.ERROR, "Invalid data.", extra_tags='alert alert-error')
        return render(request, self.template_name, {})


# def detail_session(request, pk):
#     obj = get_object_or_404(Session, pk=pk)
#     return render(request, "detail_session.html", {"session": obj})

class SessionDetailView(DetailView):
    model = Session
    template_name = 'detail_session.html'



# def create_session(request):
#     context = dict()
#
#     my_form = SessionForm(request.POST or None)
#     context["form"] = my_form
#
#     if request.method == 'POST':
#         if my_form.is_valid():
#             my_form.save()
#             print("Saved!")
#
#     return render(request, "session_form.html", context)

class CreateSession(CreateView):
    model = Session
    fields = '__all__'
    success_url = '/'
    template_name = 'session_form.html'


# def edit_session(request, pk):
#     obj = get_object_or_404(Session, pk=pk)
#     # context = {}
#
#     if request.method == "POST":
#         my_form = SessionForm(request.POST, instance=obj)
#         if my_form.is_valid():
#             my_form.save()
#             return redirect("home")
#     return render(request, "session_form.html", {"form": SessionForm(instance=obj)})

class EditSession(UpdateView):
    model = Session
    fields = '__all__'
    success_url = '/'
    template_name = 'session_form.html'



# def delete_session(request, pk):
#     obj = get_object_or_404(Session, pk=pk)
#     if request.method == "POST":
#         obj.delete()
#         return redirect("all-sessions")
#     return render(request, "confirm.html", {"session": obj})

class DeleteSession(DeleteView):
    model = Session
    success_url = '/'
    template_name = 'confirm.html'





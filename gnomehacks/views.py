from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import HackfestForm, LocationForm, RegisterForm
from .models import Attendee, Hackfest, Location


def index(request):
    latest = Hackfest.objects.order_by("-start")[:100]
    context = {"latest_hackfests": latest}
    return render(request, "gnomehacks/index.html", context)


def hackfest_detail(request, hackfest_id):
    hackfest = get_object_or_404(Hackfest, id=hackfest_id)
    attendees = Attendee.objects.filter(hackfest=hackfest)
    context = {"hackfest": hackfest, "attendees": attendees}
    return render(request, "gnomehacks/hackfest.html", context)


def location_detail(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    context = {"location": location}
    return render(request, "gnomehacks/location.html", context)


@login_required
def create_location(request):
    if request.method == "GET":
        context = {"form": LocationForm()}
        return render(request, "gnomehacks/location_form.html", context)
    elif request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(f"{obj.id}/")
        else:
            return render(request, "gnomehacks/location_form.html", {"form": form})
    return redirect("index")


@login_required
def create_hackfest(request):
    if request.method == "GET":
        context = {"form": HackfestForm()}
        return render(request, "gnomehacks/hackfest_form.html", context)
    elif request.method == "POST":
        form = HackfestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.organizer = request.user
            obj.save()
            att = Attendee.objects.create(hackfest_id=obj.id, user_id=request.user.id)
            att.save()
            return redirect(f"{obj.id}/")
        else:
            return render(request, "gnomehacks/hackfest_form.html", {"form": form})


class HacksLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "You have signed up successfully.")
            login(request, user)
            return redirect("")
        else:
            return render(request, "registration/register.html", {"form": form})


def list_locations(request):
    latest = Location.objects.all()
    context = {"locations": latest}
    return render(request, "gnomehacks/location_list.html", context)

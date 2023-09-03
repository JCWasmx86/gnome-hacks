from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hackfests/<int:hackfest_id>/", views.hackfest_detail, name="hackfest-detail"),
    path("locations/<int:location_id>/", views.location_detail, name="location-detail"),
    path("hackfests/create", views.create_hackfest, name="hackfests-create"),
    path("locations/create", views.create_location, name="location-create"),
    path("locations", views.list_locations, name="location-list"),
    path("admin/", admin.site.urls),
    path("login/", views.HacksLoginView.as_view(), name="login"),
    path("register/", views.sign_up, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

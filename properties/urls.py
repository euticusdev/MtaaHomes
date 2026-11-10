from django.urls import path
from . import views


urlpatterns = [
    path("", views. home, name="home"),
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("properties/new/", views.create_property, name="create_property"),
    path("properties/<int:pk>/", views.property_detail, name="property_detail"),
]
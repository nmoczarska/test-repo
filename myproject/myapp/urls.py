from django.urls import path

from . import views

urlpatterns = [
    path("welcome", views.welcome_view),
    path("person", views.person_list)
]
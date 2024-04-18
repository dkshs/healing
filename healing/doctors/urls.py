from django.urls import path

from . import views

urlpatterns = [
    path(
        "medical_registration/",
        views.medical_registration,
        name="medical_registration",
    ),
]

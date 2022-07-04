from django.urls import path

from animals.views import AnimalIdView, AnimalView

urlpatterns = [
    path("animals/", AnimalView.as_view()),
    path("animals/<int:animal_id>/", AnimalIdView.as_view())
]
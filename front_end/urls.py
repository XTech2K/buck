from django.urls import path
from front_end import views

urlpatterns = [
    path("", views.home, name="home"),
    path("buck/", views.lobby, name="buck lobby"),
    path("buck/<int:id>/", views.game, name="buck game")
]
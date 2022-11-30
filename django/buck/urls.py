from django.urls import path
from buck import views

urlpatterns = [
    path("", views.home, name="home"),
]
import os

from database import Database
from django.shortcuts import render
from django.http import HttpResponse

db = Database()

def get_html(filename):
    file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "html", "{}".format(filename)))
    return file.read()

def home(request):
    return HttpResponse("Hello, Django!")

def lobby(request):
    return HttpResponse("Lobby not implemented yet!")

def game(request, id):
    json = db.get_game(id).to_json(pretty=True)
    html = get_html("game.html")
    return HttpResponse(html.format(id=id, json=json))

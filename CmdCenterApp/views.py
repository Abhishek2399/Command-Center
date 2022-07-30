from http import server
from django.shortcuts import render, HttpResponse, redirect
from flask import redirect
from .models import *
# Create your views here.
def home(requests):
    return render(requests, "UI.html")

def fill_data(requests):
    actions = ["Start", "Stop"]
    app_objs = Application.objects.all()
    for app in app_objs:
        for action in actions:
            Action.objects.create(
                action_name = action,
                application = app
            )
    return redirect('admin/')
from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    url = "https://api.pandascore.co/lol/matches/"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer tLveRWByUbBtcxFDHcfIltXm6R-0iuJlbSoGfZTMIYT0ufQUrbM"
    }

    response = requests.get(url, headers=headers)

    return HttpResponse(response.text)

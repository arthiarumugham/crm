""" views.py contains all the views relevant to Tickets """
from django.shortcuts import render

# Create your views here.
def show_tickets(request):
    """ Lists all the tickets """
    return render(request, "tickets.html")

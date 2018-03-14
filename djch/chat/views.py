from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "index.html", {
        "rooms": rooms,
    })


@login_required
def chat_view(request, id):
    room = get_object_or_404(Room, id=id)

    return render(request, "chat.html", {
        "room": room,
    })

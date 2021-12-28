import json
from django.shortcuts import render
from django.core import serializers
from purewish.models import Messages

# Create your views here.


def direct_chat(request):
    return render(request, 'chat/direct_chat.html')


def room(request, room_name):
    username = "Moses"
    context = {'room_name': room_name,
               'username': username, 'messages': Messages.objects.filter(room=room_name)[0:25]}
    return render(request, 'chat/room.html', context)

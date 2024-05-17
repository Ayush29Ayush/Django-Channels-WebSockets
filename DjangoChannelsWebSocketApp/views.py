from django.shortcuts import render
from .models import Group, Chat

def index(request, group_name):
    print("Group Name...", group_name)
    #! First Check if Group Exists
    group = Group.objects.filter(name = group_name).first()
    chats=[]
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name = group_name)
        group.save()
    # return render(request, "DjangoChannelsWebSocketApp/index.html")
    # return render(request, "DjangoChannelsWebSocketApp/django_channel_layers.html")
    # return render(request, "DjangoChannelsWebSocketApp/django_channel_layers_dynamic_group_name.html", {"groupname": group_name})
    return render(request, "DjangoChannelsWebSocketApp/django_channel_database.html", {"groupname": group_name, 'chats':chats})

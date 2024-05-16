from django.shortcuts import render


def index(request, group_name):
    print("Group Name...", group_name)
    # return render(request, "DjangoChannelsWebSocketApp/index.html")
    return render(
        request,
        "DjangoChannelsWebSocketApp/django_channel_layers.html",
        {"groupname": group_name},
    )

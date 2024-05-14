from django.shortcuts import render


def index(request):
    # return render(request, "DjangoChannelsWebSocketApp/index.html")
    return render(request, "DjangoChannelsWebSocketApp/django_channel_layers.html")

from datetime import UTC, datetime

from django.contrib import messages
from django.shortcuts import render


def test_view(request):
    my_list = [
        "laptop",
        "mouse",
        "keyboard",
        "monitor",
        "printer",
        "headphones",
        "webcam",
        "microphone",
        "speakers",
        "USB hub",
    ]
    context = {"my_list": my_list, "today": datetime.now(UTC)}
    template = "detail-view.html"

    messages.add_message(request, messages.INFO, "This is a test message 1.")
    messages.add_message(request, messages.INFO, "This is a test message 2.")
    return render(request, template, context)

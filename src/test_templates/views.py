from datetime import datetime

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
    context = {
        "view_title": "This is a test view.",
        "my_number": 396,
        "my_number2": 777,
        "my_list": my_list,
        "today": datetime.now(datetime.UTC),
    }
    # template = "test_templates/test_view.html"
    # template = "test_templates/test_view2.html"
    template = "test_templates/detail-view.html"

    messages.add_message(request, messages.INFO, "This is a test message 1.")
    messages.add_message(request, messages.INFO, "This is a test message 2.")
    return render(request, template, context)

from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):

    name = "Raoul"
    HTML_STRING = f"""
    <h1>{name} HI<h1>"""
    return HttpResponse(HTML_STRING)


def home(request):
    return render(request, 'erp/inventory.html')
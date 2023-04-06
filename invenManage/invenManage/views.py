from django.http import HttpResponse


def home_view(request):

    name = "Raoul"
    HTML_STRING = f"""
    <h1>{name} HI<h1>"""
    return HttpResponse(HTML_STRING)
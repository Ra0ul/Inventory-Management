from django.http import HttpResponse

HTML_STRING = """
<h1>HI<h1>
"""


def home_view(request):
    return HttpResponse(HTML_STRING)
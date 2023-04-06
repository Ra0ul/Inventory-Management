from django.shortcuts import render, redirect

from django.http import HttpResponse

def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

# Create your views here.

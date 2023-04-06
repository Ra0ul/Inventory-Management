from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Account

def sign_in_view(request):
    if request.method == 'GET':
        account_obj = Account.objects.get(id=2)
        account_name = account_obj.name
        account_content = account_obj.content
        
        return render(request, 'accounts/login.html')

# Create your views here.

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login

def sign_up(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        
            return render(request, 'accounts/signup.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/signup.html')

# def sign_in_view(request):
#     if request.method == 'GET':
#         account_obj = Account.objects.get(id=2)
#         account_name = account_obj.name
#         account_content = account_obj.content
        
#         return render(request, 'accounts/login.html')

# Create your views here.

from django.shortcuts import render, redirect
# from .forms import NewUserForm
from .models import AccountModel

from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        
        if password != password2:
            print("비밀번호가 다릅니다.")
            return render(request, 'accounts/signup.html')
        else:
            me = get_user_model().objects.filter(username=username)  # get방식으로 조회를 하면 유저가 없을 시 오류!
            if me:
                print("이미 존재하는 아이디 입니다.")
                return render(request, 'accounts/signup.html')
            else:
                AccountModel.objects.create_user(username=username, password=password)
                return redirect('/sign-in')
    
    #폼으로 쓰려고 했지만 망함   
    # elif request.method == 'POST':
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
        
    #         return render(request, 'accounts/signup.html')
        

# def sign_in_view(request):
#     if request.method == 'GET':
#         account_obj = Account.objects.get(id=2)
#         account_name = account_obj.name
#         account_content = account_obj.content
        
#         return render(request, 'accounts/login.html')

# Create your views here.

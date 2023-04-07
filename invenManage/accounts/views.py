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
        username = request.POST.get('username', 'None')
        password = request.POST.get('password', 'None')
        password2 = request.POST.get('password2', 'None')
        
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
        

def sign_in(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        
        #아이디와 비밀번호가 맞으면 기본 페이지 inventory.html로
        #아니면 다시 로그인
        
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')

    

        return redirect(request, 'accounts/login.html')


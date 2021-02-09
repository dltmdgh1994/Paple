
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Member
from .forms import MemberJoinForm, LogInForm


def signup(request):
    signup_form = MemberJoinForm()
    if request.method == "POST":
        form = MemberJoinForm(request.POST)
        mem_list = Member.objects.all()
        if mem_list.filter(user_email=request.POST['user_email']).exists():
            return render(request, 'account/signup.html', {'message': '이미 존재하는 이메일 입니다.',
                                                           'signup_form': signup_form})
        if request.POST['user_pw1'] != request.POST['user_pw2']:
            return render(request, 'account/signup.html', {'message': '비밀번호가 일치하지 않습니다.',
                                                           'signup_form': signup_form})
        else:
            if form.is_valid():
                form.save(commit=False)
                return render(request, 'account/signup_done.html', {'message': '회원가입 성공'})

            else:
                return render(request, 'account/signup.html',
                              {'message': '회원가입 실패',
                               'signup_form': signup_form
                               })

    if request.method == "GET":
        return render(request, 'account/signup.html', {'signup_form': signup_form})


def login(request):
    login_form = LogInForm()
    if request.method == 'POST':
        input_email = request.POST['user_email']
        input_pw = request.POST['user_pw1']

        if Member.objects.filter(user_email=input_email).exists():
            getUser = Member.objects.get(user_email=input_email)
            if getUser.user_pw1 == input_pw:
                # request.session['loginObj'] = True
                request.session['loginObj'] = getUser.user_email
                # group이 있고없고 조건으로 나눠야 함
                return redirect('/bbs/main/')
            else:
                return render(request, 'account/login.html', {
                    'message': '비밀번호가 맞지 않습니다.',
                    'login_form': login_form
                })
        else:
            return render(request, 'account/login.html', {
                'message': '존재하지 않는 이메일 입니다.',
                'login_form': login_form
            })

    if request.method == 'GET':
        return render(request, 'account/login.html', {'login_form': login_form})


def signupdone(request):
    return render(request, 'account/signup_done.html')

#
# def logout(request):
#     request.session.clear()
#     return render(request, 'index.html')


# def login(request):
#     if request.method == 'POST':
#         input_email = request.POST['user_email']
#         input_pw = request.POST['user_pw1']
#         user = auth.authenticate(request, user_email=input_email, user_pw1=input_pw)
#         if user is not None:
#             auth.login(request, user)
#             user_dict = {
#                 'u_email': user.user_email,
#                 'u_name': user.user_name,
#                 'u_birth': user.user_birth
#             }
#             request.session['loginObj'] = user_dict
#             # group이 있고없고 조건으로 나눠야 함
#             return render(request, 'account/login.html', {'message': '로그인 성공!'})
#         else:
#             return render(request, 'account/login.html', {'message': '로그인 실패!'})
#
#     if request.method == 'GET':
#         login_form = LogInForm()
#         return render(request, 'account/login.html', {'login_form': login_form})

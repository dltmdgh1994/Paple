
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
                form.save()
                return render(request, 'account/signup_done.html', {'message': '회원가입 성공'})

            else:
                return render(request, 'account/signup.html',
                              {'message': '회원가입 실패',
                               'signup_form': signup_form
                               })

    if request.method == "GET":
        return render(request, 'account/signup.html', {'signup_form': signup_form})


def login(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        user_pw = request.POST['user_pw1']
        user = auth.authenticate(request, user_email=user_email, user_pw1=user_pw)
        if user is not None:
            auth.login(request, user)
            user_dict = {
                'u_email': user.user_email,
                'u_name': user.user_name,
                'u_birth': user.user_birth
            }
            request.session['loginObj'] = user_dict
            # group이 있고없고 조건으로 나눠야 함
            return render(request, 'account/login.html', {'message': '로그인 성공!'})
        else:
            return render(request, 'account/login.html', {'message': '로그인 실패!'})

    if request.method == 'GET':
        login_form = LogInForm()
        return render(request, 'account/login.html', {'login_form': login_form})

def signupdone(request):
    return render(request, 'account/signup_done.html')


# # Create your views here.
# def signup(request):
#
#     if request.method == "POST":
#         try:
#             user_form = UserCreateForm(request.POST)
#             # if user_form.is_valid():
#             # username = request.POST['username']
#             email = request.POST['email']
#             # password = request.POST['password1']
#             new_user = User.objects.create_user(email)
#             new_user.save()
#             # user_form.save()
#             # login(request, user_form)
#             return redirect('index.html')
#         # return render(request, 'bbs/signup.html')
#         #     else:
#         #         return render(request, 'index.html', {'error_message': '회원가입에 실패했습니다.'})
#         except:
#             render(request, 'bbs/signup.html', {'message': '회원이 이미 있음'})
#
#     if request.method == "GET":
#         user_form = UserCreateForm()
#         return render(request, 'bbs/signup.html', {'user_form': user_form})
#
# # 이메일 중복 검사
# # if User.objects.filter(email= request.POST['user_email']).exist():
# #     context = {
# #         'error_message': "이미 존재하는 이메일 입니다."
# #     }
# #     return render(request, 'bbs/signup.html', context)
# #
# # else:
# #
# # if request.POST["password1"] == request.POST["password2"]:
# #     user = User.objects.create_user(
# #         username=request.POST["username"]
# #     )
# # auth.login(request, user)




  #
        # if form.is_valid():
        #     if request.POST['user_pw1'] == request.POST['user_pw2']:
        #         form.save()
        #         context = {
        #             'message': '회원가입에 성공했습니다.'
        #         }
        #         return render(request, 'account/signup_done.html', context)
        #     else:
        #         context = {
        #             'message': '비밀번호가 일치하지 않습니다.'
        #         }
        #         return render(request, 'account/signup_done.html', context)
        # else:
        #     context = {
        #         'message': '양식이 유효하지 않습니다.'
        #     }
        #     return render(request, 'account/signup_done.html', context)

#
#
# def signup(request):
#     if request.method == "POST":
#
#         try:
#             form = MemberJoinForm(request.POST)
#             # useremail = request.POST.get('user_email')
#             # username = request.POST.get['user_name']
#             # password = request.POST.get['user_pw1']
#             # re_password = request.POST.get['user_pw2']
#             # userbirth = request.POST.get['user_birth']
#             # message = {}
#             #
#             # if password != re_password:
#             #     message['error'] = '비밀번호가 일치하지 않습니다.'
#             # else:
#             #     new_user = Member(
#             #         user_email = useremail,
#             #         group_id= 'default',
#             #         user_name= username,
#             #         user_pw1=password,
#             #         user_pw2=re_password,
#             #         user_birth=userbirth
#             #     )
#             #     new_user.save()
#
#             form.save()
#             context = {
#                 'message': '회원가입 성공!!!!!!!!!!!'
#             }
#             return render(request, 'account/signup_done.html', context)
#
#         except:
#             return render(request, 'account/signup_done.html', {'message': '회원가입 실패'})
#
#     if request.method == "GET":
#         form = MemberJoinForm()
#         return render(request, 'account/signup.html', {'signup_form': form})
#
# def login(request):
#     return render(request, 'account/login.html')
#
# def signupdone(request):
#     return render(request, 'account/signup_done.html')
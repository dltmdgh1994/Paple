from django.shortcuts import render, get_object_or_404, redirect
from account.models import Member, Group
from group.forms import ModifyGroupInfoForm, GroupForm
import uuid
import base64
import codecs


def group_main(request):
    return render(request, 'group/group_main.html')


def group_login(request):
    if request.method == "POST":

        # 초대 코드를 통해 그룹 찾기
        val = request.POST.get("invite_code")
        try:
            group = Group.objects.get(group_code=val)
        except Group.DoesNotExist:
            return render(request, 'group/group_main.html', {
                'message': '초대 코드가 잘못됐습니다.'
            })

        user_email = request.session['loginObj']
        member = Member.objects.get(user_email=user_email)
        member.group_code = group
        member.user_status = True
        member.save()

        return redirect('bbs:main')


def group_signin(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            # Group 정보 수정
            form.save()
            
            # Member 정보 수정
            user_email = request.session['loginObj']
            member = Member.objects.get(user_email=user_email)
            group = Group.objects.get(group_code=form.cleaned_data['group_code'])
            member.group_code = group
            member.user_status = True
            member.save()

            return redirect('bbs:main')
    else:
        form = GroupForm()
        invite_code = generate_random_slug_code()

        return render(request, 'group/group_signin.html', {
            'form': form,
            'invite_code': invite_code
        })


def group_modify(request):
    login_email = request.session['loginObj']
    member = get_object_or_404(Member, pk=login_email)
    group = get_object_or_404(Group, pk=member.group_code)
    group_members = Member.objects.filter(group_code=member.group_code)
    modify_form = ModifyGroupInfoForm(instance=group)

    if request.method == 'POST':
        group_list = Group.objects.all()
        if (group_list.filter(group_code=request.POST['group_code']).exists()) & (group.group_code != request.POST['group_code']):
            return render(request, 'group/group_modify.html', {'message': '이미 존재하는 그룹 이름 입니다.',
                                                               'modify_form': modify_form,
                                                               'group_members': group_members,
                                                               'group': group
                                                               })

        modify_form = ModifyGroupInfoForm(request.POST, instance=group)
        if modify_form.is_valid():
            modify_form.save()
            return render(request, 'group/group_modify.html', {
                'message': '그룹정보 update 완료!',
                'group_members': group_members,
                'group': group,
                'modify_form': modify_form
            })
        else:
            return render(request, 'group/group_modify.html', {
                'message': '그룹정보 update 실패',
                'modify_form': modify_form
            })

    if request.method == 'GET':
        return render(request, 'group/group_modify.html', {'modify_form': modify_form,
                                                           'group_members': group_members,
                                                           'group': group})


def generate_random_slug_code(length=8):
    """
    generates random code of given length
    """
    return base64.urlsafe_b64encode(
        codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
    ).decode()[:length]
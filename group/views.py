from django.shortcuts import render, get_object_or_404
from account.models import Member, Group
from group.forms import ModifyGroupInfoForm


def group_main(request):

    return render(request, 'group/group_main.html', {
        'page_title': 'Group_Main',
        'user_data': '그룹 만들기'
    })


def group_modify(request):
    login_email = request.session['loginObj']
    member = get_object_or_404(Member, pk=login_email)
    group = get_object_or_404(Group, pk=member.group_name)
    group_members = Member.objects.filter(group_name=member.group_name)
    modify_form = ModifyGroupInfoForm(instance=group)

    if request.method == 'POST':
        group_list = Group.objects.all()
        if group_list.filter(group_name=request.POST['group_name']).exists():
            return render(request, 'group/group_modify.html', {'message': '이미 존재하는 그룹 이름 입니다.',
                                                               'modify_form': modify_form})
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




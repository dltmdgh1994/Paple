from django.shortcuts import render


def group_main(request):

    return render(request, 'group/group_main.html', {
        'page_title' : 'Group_Main',
        'user_data' : '그룹 만들기'
    })


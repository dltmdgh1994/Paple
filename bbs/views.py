from django.shortcuts import render, redirect, get_object_or_404
from bbs.models import Question, Post
from account.models import Group, Member
from django.core.paginator import Paginator


def main(request):
    try:
        user_email = request.session['loginObj']
        if user_email:
            # login_obj = request.session['loginObj']
            questions = Question.objects.all().order_by('q_date')
            q_list = [q.as_dict() for q in questions]

            return render(request, 'bbs/main.html', {
                'q_list': q_list
            })
        else:
            return redirect('/')

    except:
        return redirect('/')


def logout(request):
    if request.session['loginObj']:
        del (request.session['loginObj'])
    return redirect('/')


def board(request):
    # 해당 그룹의 게시판 글을 DB에서 불러옴
    user_email = request.session['loginObj']
    member = get_object_or_404(Member, pk=user_email)
    group_name = member.group_name

    posts = Post.objects.filter(group_name=group_name).order_by('-post_id')

    page = request.GET.get('page', '1')

    # 페이지 당 게시물 개수 지정
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {'posts': page_obj}

    return render(request, 'bbs/board.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'bbs/detail.html')

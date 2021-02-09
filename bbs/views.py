from django.shortcuts import render, redirect, get_object_or_404
from bbs.models import Question, Post
from django.core.paginator import Paginator
from django.contrib import auth


def main(request):
    login_obj = request.session['loginObj']
    if request.method == "GET":
        return render(request, 'index.html')

    elif request.method == "POST":
        if login_obj:
            group_name = login_obj['group_name']
            questions = Question.objects.filter(group_name=group_name).order_by('q_date')
            q_list = [q.as_dict() for q in questions]

            return render(request, 'bbs/main.html', {'q_list': q_list})
        else:
            return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def board(request):
    # DB의 모든 글의 내용을 들고 옴
    posts = Post.objects.all().order_by('-post_id')

    page = request.GET.get('page', '1')

    # 페이지 당 게시물 개수 지정
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {'posts': page_obj}

    return render(request, 'bbs/board.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'bbs/detail.html')



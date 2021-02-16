from django.shortcuts import render, redirect, get_object_or_404
from bbs.models import Question, Post, Comment
from account.models import Group, Member
from django.core.paginator import Paginator
from .forms import PostForm
import datetime


def main(request):
    try:
        user_email = request.session['loginObj']
    except:
        return redirect('/')

    if user_email:
        # 달력 질문 리스트
        questions = Question.objects.all().order_by('q_date')
        q_list = [q.as_dict() for q in questions]

        # 올라온 질문
        member = get_object_or_404(Member, pk=user_email)
        group_name = member.group_name
        posts = Post.objects.filter(group_name=group_name).order_by('-post_id')[0:2]

        # 오늘의 질문
        today_date = datetime.date.today().isoformat()
        try:
            today_q = Question.objects.get(q_date=today_date)
        except Question.DoesNotExist:
            today_q = None

        return render(request, 'bbs/main.html', {
            'q_list': q_list,
            'posts': posts,
            'today_q': today_q,
        })
    else:
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

    user_email = request.session['loginObj']
    member = get_object_or_404(Member, pk=user_email)
    group_name = member.group_name
    comments = Comment.objects.filter(group_name=group_name, post_id=post_id)

    return render(request, 'bbs/detail.html', {
        'post': post,
        'comments': comments
    })


def post_register(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user_email = request.session['loginObj']
            member = Member.objects.get(user_email=user_email)
            group_name = member.group_name
            post.user_email = member
            post.group_name = group_name
            post.post_date = datetime.datetime.now()
            post.save()
            return redirect('bbs:board')
    else:
        form = PostForm()

    return render(request, 'bbs/post_register.html', {
        'form': form
    })


def post_update(request, post_id):
    post = Post.objects.get(post_id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            user_email = request.session['loginObj']
            member = Member.objects.get(user_email=user_email)
            group_name = member.group_name
            post.user_email = member
            post.group_name = group_name
            post.post_date = datetime.datetime.now()
            post.save()

            return redirect('bbs:detail', post_id=post_id)
    else:
        form = PostForm(instance=post)

    return render(request, 'bbs/post_update.html', {
        'form': form
    })


def post_delete(request, post_id):
    post = Post.objects.get(post_id=post_id)
    post.delete()
    return redirect('bbs:board')


def comment_register(request, post_id):
    if request.method == 'POST':
        val = request.POST.get("comment")
        user_email = request.session['loginObj']
        member = Member.objects.get(user_email=user_email)
        group_name = member.group_name
        post = Post.objects.get(post_id=post_id)

        comment = Comment()
        comment.user_email = member
        comment.group_name = group_name
        comment.c_content = val
        comment.post_id = post
        comment.save()

        return redirect('bbs:detail', post_id=post_id)


def question_register(request, q_id):
    question = Question.objects.get(q_id=q_id)

    try:
        post = Post.objects.get(post_name=question.q_content)
    except Post.DoesNotExist:
        post = None

    if post is None:
        post = Post()
        user_email = request.session['loginObj']
        member = Member.objects.get(user_email=user_email)
        group_name = member.group_name
        post.user_email = member
        post.group_name = group_name
        post.post_date = datetime.datetime.now()
        post.post_name = question.q_content
        post.post_content = " "
        post.save()

        return redirect('bbs:detail', post_id=post.post_id)
    else:
        return redirect('bbs:detail', post_id=post.post_id)


def question_register2(request, q_date):
    try:
        question = Question.objects.get(q_date=q_date)
    except Question.DoesNotExist:
        return redirect('bbs:main')

    try:
        post = Post.objects.get(post_name=question.q_content)
    except Post.DoesNotExist:
        post = None

    if post is None:
        post = Post()
        user_email = request.session['loginObj']
        member = Member.objects.get(user_email=user_email)
        group_name = member.group_name
        post.user_email = member
        post.group_name = group_name
        post.post_date = datetime.datetime.now()
        post.post_name = question.q_content
        post.post_content = " "
        post.save()

        return redirect('bbs:detail', post_id=post.post_id)
    else:
        return redirect('bbs:detail', post_id=post.post_id)

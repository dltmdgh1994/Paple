from django.shortcuts import render, redirect, get_object_or_404
from bbs.models import Group, Question
import json


# Create your views here.
def main(request):
    questions = Question.objects.all().order_by('q_date')
    q_list = [q.as_dict() for q in questions]

    return render(request, 'bbs/main.html', {'q_list': q_list})

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse("Hi, my love. But also %s." % output)


def detail(request, question_id):
    return HttpResponse("This is question: %s." % question_id)


def results(request, question_id):
    response = "You're looking at the result of %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on %s." % question_id)

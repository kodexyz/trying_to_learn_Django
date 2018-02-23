from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi, my love")


def detail(request, question_id):
    return HttpResponse("This is question: %s." % question_id)


def results(request, question_id):
    response = "You're looking at the result of %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on %s." % question_id)

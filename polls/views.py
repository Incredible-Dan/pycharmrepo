from django.shortcuts import render, HttpResponse
from .models import Question

from decouple import config
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, "polls/index.html", context)


def environment(request):
    return HttpResponse(config('ENVIRONMENT'))

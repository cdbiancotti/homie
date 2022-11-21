
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    ## Large version
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     return Http404('Question does not exist')
    
    ## Short version with shortcut
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "Options for Question id %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Question %s voted." % question_id)
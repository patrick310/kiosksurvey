from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Option


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'surveys/index.html', context)


def survey_administration(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'surveys/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_option = question.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'surveys/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_option.votes += 1
        selected_option.save()

        return HttpResponseRedirect(reverse('surveys:detail', args=(question.id,)))

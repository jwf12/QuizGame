from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Answer2, Category
from django.urls import reverse
from django.views import generic


def index (request):
    contexto = {}
    questions = Question.objects.all()
    contexto['latest_questions'] = questions
    return render(request, 'polls/index.html', contexto)



class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = "polls/answ.html"
    context_object_name = 'latest_questions'


def category_detail(request, category_id):
    contexto = {}
    selected_category = Category.objects.get(pk = category_id)
    contexto['selected_category'] = selected_category

    c= Question.objects.filter(category = selected_category)
    contexto['cat_quest'] = c
    return render(request, 'polls/answ.html', contexto)


def results (request, question_id):
    contexto = {}
    latest_questions = Question.objects.get(pk = question_id)
    contexto['latest_questions'] = latest_questions

    c= Choice.objects.filter(question = latest_questions)
    contexto['latest_ans'] = c
    return render(request, 'polls/results.html', contexto)


def vote(request, question_id):
    latest_questions = Question.objects.get(pk = question_id)
    right_ans = Answer2.objects.get(choice = latest_questions)

    try:
        selected_choice= latest_questions.choice_set.get(pk= request.POST['choice'])


    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/answ.html", {
            'latest_questions': latest_questions,
            'error_massage': 'No elegiste una respuesta',
        })

    else:
        if selected_choice.choice_text == right_ans.answer_text:
            return render ( request, 'polls/results.html')
        else:
            return HttpResponseRedirect(reverse('polls:index'))

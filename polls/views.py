from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Category, Answer2
from django.urls import reverse
from django.views import generic


def index(request):
    contexto = {}
    all_category = Category.objects.all()
    contexto['all_category'] = all_category
    return render(request, 'polls/index.html', contexto)


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/answ.html"
    context_object_name = 'latest_questions'


def detail_view(request, category_id):
    contexto = {}
    selected_category = Category.objects.get(pk = category_id)
    contexto['selected_category'] = selected_category
    
    cat_questions = Question.objects.filter(category = selected_category)
    contexto['cat_questions'] = cat_questions
    return render(request, 'polls/answ.html', contexto)


# def results(request, question_id):
#     contexto = {}
#     latest_questions = Question.objects.get(pk = question_id)
#     contexto['latest_questions'] = latest_questions

#     c= Choice.objects.filter(question = latest_questions)
#     contexto['latest_ans'] = c
#     return render(request, 'polls/results.html', contexto)
    

def vote(request, question_id):
    latest_questions = Question.objects.get(pk = question_id)
    right_ans = Answer2.objects.get(choice = latest_questions)

    try:
        selected_choice= latest_questions.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/answ.html", {
            'latest_questions': latest_questions,
            'error_massage': 'No elegiste una respuesta',
        })

    else:
        if selected_choice.choice_text == right_ans.answer_text:
            return redirect('polls:results', question_id=question_id)
        else:
            return redirect('polls:index')
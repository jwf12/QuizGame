from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Answer2, Category
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect


def index(request):
    contexto = {}
    all_category = Category.objects.all()
    contexto['all_category'] = all_category
    return render(request, 'polls/index.html', contexto)


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/answ.html"
#     context_object_name = 'latest_questions'


def question_detail_view(request, category_id):
    contexto = {}
    selected_category = Category.objects.get(pk = category_id)
    contexto['selected_category'] = selected_category

    cat_questions= Question.objects.filter(category = selected_category)
    contexto['cat_questions'] = cat_questions
    return render(request, 'polls/answ.html', contexto)


# def results (request, question_id):
#     contexto = {}
#     latest_questions = Question.objects.get(pk = question_id)
#     contexto['latest_questions'] = latest_questions

#     c= Choice.objects.filter(question = latest_questions)
#     contexto['latest_ans'] = c
#     return render(request, 'polls/results.html', contexto)
    

def vote(request, question_id):
    latest_questions = Question.objects.get(pk = question_id)
    right_ans = Answer2.objects.get(choice = latest_questions)

    if request.method == 'POST':
        choice = request.POST.get('choice', None)
        if not choice:
            # if the user doesn't select a choice
            context = {
            'question': latest_questions,
            'error_massage': 'No elegiste una respuesta',
            }
            return render(request, 'polls/results.html', context=context)

        # if there is a selected choice
        # here we can use get_object_or_404()
        selected_choice = latest_questions.choice_set.get(pk=choice)

        context = {
            'question': latest_questions,
            'right_ans': right_ans,
            'selected_choice': selected_choice,
        }
        return render(request, 'polls/results.html', context=context)
    # if it's a get request
    return redirect('polls:index')

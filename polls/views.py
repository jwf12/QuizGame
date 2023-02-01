from django.shortcuts import render
from .models import Question, Choice, Answer2, Category
from django.core.paginator import (Paginator,EmptyPage,PageNotAnInteger)


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
    
    page = request.GET.get('page', 1)

    global paginator
    pagi = Paginator(cat_questions, 1)
    paginator = pagi

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(1)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)


    contexto['paginator'] = items_page
    
    return render(request, 'polls/answ.html', contexto)


# def results (request, question_id):
#     contexto = {}
#     latest_questions = Question.objects.get(pk = question_id)
#     contexto['latest_questions'] = latest_questions

#     c= Choice.objects.filter(question = latest_questions)
#     contexto['latest_ans'] = c
#     return render(request, 'polls/results.html', contexto)
    

def vote(request, question_id):
    latest_question = Question.objects.get(pk = question_id)
    right_ans = Answer2.objects.get(choice = latest_question)
    paginator
    
    try:
        selected_choice = latest_question.choice_set.get(pk = request.POST['choice'])   
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/results.html", {
            'latest_questions': latest_question,
            'error_massage': 'No elegiste una respuesta, volve para atras <--',
        })

    else:        
        return render(request, 'polls/results.html',{
            'right_ans': right_ans,
            'selected_choice':selected_choice,
            'latest_question':latest_question,
            'paginator':paginator
        })
       
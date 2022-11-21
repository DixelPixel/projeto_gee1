from django.shortcuts import render
from groups.model.groups import Group
from groups.questions.questions import Question
from groups.questions.answer import Answer
from .forms import AnswersForm
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect

from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)


# Create your views here.

def index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {
        'groups': groups
    })


def group_details(request, group_slug):
    try:
        selected_group = Group.objects.get(slug=group_slug)
        return render(request, 'groups/group-details.html', {
            'group_found': True,
            'group_name': selected_group.title,
            'group_description': selected_group.description,
            'group_date': selected_group.date,
            'group_organizer_email': selected_group.organizer_email
        })
    except Exception as exc:
        return render(request, 'groups/group-details.html', {
            'group_found': False
        })


# Admin - senha: BRUH

def landing_page(request):
    return render(request, 'groups/logo.html')


@csrf_protect
def questionario(request):
    questions = Question.objects.all()
    form = AnswersForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:

        print("OK!!")
        answer1 = request.POST.get('1', 1)
        answer2 = request.POST.get('2', 2)
        answer3 = request.POST.get('3', 3)
        answer4 = request.POST.get('4', 4)
        answer5 = request.POST.get('5', 5)
        answer6 = request.POST.get('6', 6)
        answer7 = request.POST.get('7', 7)
        answer8 = request.POST.get('8', 8)
        answer9 = request.POST.get('9', 9)
        answer10 = request.POST.get('10', 10)
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        new_answer1 = Answer.objects.create(answer=answer1, question=questions[0])
        new_answer2 = Answer.objects.create(answer=answer2, question=questions[1])
        new_answer3 = Answer.objects.create(answer=answer3, question=questions[2])
        new_answer4 = Answer.objects.create(answer=answer4, question=questions[3])
        new_answer5 = Answer.objects.create(answer=answer5, question=questions[4])
        new_answer6 = Answer.objects.create(answer=answer6, question=questions[5])
        new_answer7 = Answer.objects.create(answer=answer7, question=questions[6])
        new_answer8 = Answer.objects.create(answer=answer8, question=questions[7])
        new_answer9 = Answer.objects.create(answer=answer9, question=questions[8])
        new_answer10 = Answer.objects.create(answer=answer10, question=questions[9])

    return render(request, 'groups/corpodosite.html', {
        'questions': questions,
        'num1': 1,
        'num2': 2,
        'num3': 3,
        'num4': 4,
        'num5': 5

    })


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render(request, 'groups/error.html')

def cadastro(request):
    return render(request,'groups/cadastro.html')

def login(request):
    return render(request,'groups/login.html')

def recomendacoes(request):
    return render(request,'groups/recomendacoes.html')

@csrf_protect
def questionario2(request):
    questions = Question.objects.all()
    if request.method=='POST':
        q1 = request.POST['1']
        q2 = request.POST['1']
        q3 = request.POST['3']
        q4 = request.POST['4']
        q5 = request.POST['5']
        q6 = request.POST['6']
        q7 = request.POST['7']
        q8 = request.POST['8']
        q9 = request.POST['9']
        q10 = request.POST['10']
        
        quest1 = Answer.objects.create(answer=q1,question=questions[0])
        quest2 = Answer.objects.create(answer=q2,question=questions[1])
        quest3 = Answer.objects.create(answer=q3,question=questions[2])
        quest4 = Answer.objects.create(answer=q4,question=questions[3])
        quest5 = Answer.objects.create(answer=q5,question=questions[4])
        quest6 = Answer.objects.create(answer=q6,question=questions[5])
        quest7 = Answer.objects.create(answer=q7,question=questions[6])
        quest8 = Answer.objects.create(answer=q8,question=questions[7])
        quest9 = Answer.objects.create(answer=q9,question=questions[8])
        quest10 = Answer.objects.create(answer=q10,question=questions[9])

        quest1.save()
        quest2.save()
        quest3.save()
        quest4.save()
        quest5.save()
        quest6.save()
        quest7.save()
        quest8.save()
        quest9.save()
        quest10.save()
        


    return render(request,'groups/questionario.html')

def criar_evento(request):
    return render(request,'groups/criar_evento.html')

def tela_principal(request):
    return render(request,'groups/tela_principal.html')

def landingpage(request):
    return render(request,'groups/landingpage.html')
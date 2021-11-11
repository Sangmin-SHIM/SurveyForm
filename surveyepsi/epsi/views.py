from django.shortcuts import render, get_object_or_404, redirect
from .models import Professeur, Grade, Question, Answer, Etudiant


# Create your views here.

def index(request):
    print("select1.html")

    grade = Grade.objects.all
    context = {'grade' : grade}

    return render(request, "survey/select1.html", context)


def detail(request, grade_code):
    '''
    By grade, we show the professeurs et their cours
'''

    professeur = Professeur.objects.all().filter(grade_code=grade_code)
    context = {'professeur': professeur}
    return render(request, "survey/select2.html", context)

def survey(request, grade_code, idx):
    professeur = Professeur.objects.filter(grade_code = grade_code).filter(idx = idx)
    question = Question.objects.all()



    context = {'professeur': professeur,
               'question' : question}

    return render(request, "survey/survey.html", context)

def success(request,grade_code,idx):
    professeur = get_object_or_404(Professeur, pk=idx)
    etudiant = Etudiant(professeur_idx_id=professeur.idx)
    etudiant.save()
    '''etudiant = Etudiant(professeur_idx=)
    answer = Answer.objects.all()'''



    return render(request, "survey/success.html")
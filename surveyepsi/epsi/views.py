from django.shortcuts import render, get_object_or_404, redirect
from .models import Professeur, Grade, Question, Answer, Etudiant
from django.db import IntegrityError
#################################################
# It's an app for Students to submit the Survey #
#################################################

# First Page : We can select the grade from B1 to I2
def index(request):
    grade = Grade.objects.all
    context = {'grade' : grade}

    return render(request, "survey/select1.html", context)

# Second Page : We can select the modules (courses) by grade that we choose
def detail(request, grade):

    professeur = Professeur.objects.all().filter(grade=grade)
    context = {'professeur': professeur}

    return render(request, "survey/select2.html", context)

# Third Page : We can actually be in the Survey Form along the module(course) that we choose
def survey(request, grade, idx):
    professeur = Professeur.objects.filter(grade = grade).filter(idx = idx)
    question = Question.objects.all()

    context = {'professeur': professeur,
               'question' : question}

    return render(request, "survey/survey.html", context)

# Fourth Page : If student submit his survey form by POST, the answers will be saved along the question id from 1 to 16
def success(request, grade, idx):
    ''' Etudiant'''
    professeur = get_object_or_404(Professeur, pk=idx)

    # If there is an error when submitting, we throw Exception
    try:
        etudiant = Etudiant(professeur_idx_id=professeur.idx)
        # It saves etudiant model to make a relation with 16 answers
        etudiant.save()
        answer1 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=1, professeur_idx_id=idx, response=request.POST.get('content1'))
        answer2 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=2, professeur_idx_id=idx, response=request.POST.get('question2'))
        answer3 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=3, professeur_idx_id=idx, response=request.POST.get('question3'))
        answer4 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=4, professeur_idx_id=idx, response=request.POST.get('question4'))

        answer5 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=5, professeur_idx_id=idx, response=request.POST.get('content2'))

        answer6 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=6, professeur_idx_id=idx, response=request.POST.get('question5'))
        answer7 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=7, professeur_idx_id=idx, response=request.POST.get('question6'))
        answer8 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=8, professeur_idx_id=idx, response=request.POST.get('question7'))
        answer9 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=9, professeur_idx_id=idx, response=request.POST.get('question8'))

        answer10 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=10, professeur_idx_id=idx, response=request.POST.get('content3'))

        answer11 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=11, professeur_idx_id=idx, response=request.POST.get('question9'))
        answer12 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=12, professeur_idx_id=idx, response=request.POST.get('question10'))
        answer13 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=13, professeur_idx_id=idx, response=request.POST.get('question11'))
        answer14 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=14, professeur_idx_id=idx, response=request.POST.get('question12'))
        answer15 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=15, professeur_idx_id=idx, response=request.POST.get('question13'))

        answer16 = Answer(etudiant_idx_id=etudiant.idx, question_idx_id=16, professeur_idx_id=idx, response=request.POST.get('content4'))


        answer1.save()
        answer2.save()
        answer3.save()
        answer4.save()
        answer5.save()
        answer6.save()
        answer7.save()
        answer8.save()
        answer9.save()
        answer10.save()
        answer11.save()
        answer12.save()
        answer13.save()
        answer14.save()
        answer15.save()
        answer16.save()

    except IntegrityError as i:
        # When User goes up directly the next page of survey form, like typing directly
        # (127.0.0.1:8000/epsi/B2/3/success), in this case the method POST would not be generated.
        # But, student model is still generated (in 45 lines : etudiant.save())
        # So there will be an issue that student model exists but related with it there are no answers.
        # It makes IntegrityError. So it has to be deleted here.
        etudiant.delete()
        return render("ERROR: Error /success Directly Prohibited !")

    professeur = Professeur.objects.filter(grade = grade).filter(idx = idx)
    context = {'professeur': professeur}

    return render(request, "survey/success.html", context)

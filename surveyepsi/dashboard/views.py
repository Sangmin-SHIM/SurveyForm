from django.shortcuts import render, get_object_or_404
from epsi.models import Grade, Professeur, Etudiant, Answer, Question

def index(request):

    grade = Grade.objects.all
    context= {'grade' : grade}
    return render(request,'dashboard/dashboard_index.html', context)

def detail(request, grade_code):

    professeur = Professeur.objects.all().filter(grade_code=grade_code)
    context = {'professeur': professeur}
    return render(request, "dashboard/dashboard_grade.html", context)

def result(request, grade_code, idx):

    professeur = Professeur.objects.all().filter(idx=idx)
    question = Question.objects.all()
    answer = Answer.objects.all().filter(professeur_idx_id=idx)
    etudiant_count = Etudiant.objects.all().filter(professeur_idx_id=idx).count()

    ''' Answer de QCM '''
    answer2=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=2)
    answer3=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=3)
    answer4=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=4)

    answer6=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=6)
    answer7=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=7)
    answer8=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=8)
    answer9=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=9)

    answer11=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=11)
    answer12=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=12)
    answer13=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=13)
    answer14=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=14)
    answer15=Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=15)

    '''
    for i in range(1,16):
        if (i != 1 or i != 5 or i != 10 or i != 16):
            globals()['answer' + str(i)] = Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=i)
    '''

    for i in range(1,16):
        if (i != 1 or i != 5 or i != 10 or i != 16):
            globals()['q'+str(i)+'_pas'] =[]
            globals()['q' + str(i) + '_peu'] =[]
            globals()['q' + str(i) + '_assez'] =[]
            globals()['q' + str(i) + '_tres'] =[]

    for i in range(etudiant_count):
        ''' Pas Satisfait'''
        if (str(answer2[i]) == 'Pas Satisfait'):
            q2_pas.append(answer2[i])
        if (str(answer3[i]) == 'Pas Satisfait'):
            q3_pas.append(answer3[i])
        if (str(answer4[i]) == 'Pas Satisfait'):
            q4_pas.append(answer4[i])
        if (str(answer6[i]) == 'Pas Satisfait'):
            q6_pas.append(answer6[i])
        if (str(answer7[i]) == 'Pas Satisfait'):
            q7_pas.append(answer7[i])
        if (str(answer8[i]) == 'Pas Satisfait'):
            q8_pas.append(answer8[i])
        if (str(answer9[i]) == 'Pas Satisfait'):
            q9_pas.append(answer9[i])
        if (str(answer11[i]) == 'Pas Satisfait'):
            q11_pas.append(answer11[i])
        if (str(answer12[i]) == 'Pas Satisfait'):
            q12_pas.append(answer12[i])
        if (str(answer13[i]) == 'Pas Satisfait'):
            q13_pas.append(answer13[i])
        if (str(answer13[i]) == 'Pas Satisfait'):
            q13_pas.append(answer13[i])
        if (str(answer14[i]) == 'Pas Satisfait'):
            q14_pas.append(answer14[i])
        if (str(answer15[i]) == 'Pas Satisfait'):
            q15_pas.append(answer15[i])

        ''' Peu Satisfait'''
        if (str(answer2[i]) == 'Peu Satisfait'):
            q2_peu.append(answer2[i])
        if (str(answer3[i]) == 'Peu Satisfait'):
            q3_peu.append(answer3[i])
        if (str(answer4[i]) == 'Peu Satisfait'):
            q4_peu.append(answer4[i])
        if (str(answer6[i]) == 'Peu Satisfait'):
            q6_peu.append(answer6[i])
        if (str(answer7[i]) == 'Peu Satisfait'):
            q7_peu.append(answer7[i])
        if (str(answer8[i]) == 'Peu Satisfait'):
            q8_peu.append(answer8[i])
        if (str(answer9[i]) == 'Peu Satisfait'):
            q9_peu.append(answer9[i])
        if (str(answer11[i]) == 'Peu Satisfait'):
            q11_peu.append(answer11[i])
        if (str(answer12[i]) == 'Peu Satisfait'):
            q12_peu.append(answer12[i])
        if (str(answer13[i]) == 'Peu Satisfait'):
            q13_peu.append(answer13[i])
        if (str(answer13[i]) == 'Peu Satisfait'):
            q13_peu.append(answer13[i])
        if (str(answer14[i]) == 'Peu Satisfait'):
            q14_peu.append(answer14[i])
        if (str(answer15[i]) == 'Peu Satisfait'):
            q15_peu.append(answer15[i])

        ''' Assez Satisfait'''
        if (str(answer2[i]) == 'Assez Satisfait'):
            q2_assez.append(answer2[i])
        if (str(answer3[i]) == 'Assez Satisfait'):
            q3_assez.append(answer3[i])
        if (str(answer4[i]) == 'Assez Satisfait'):
            q4_assez.append(answer4[i])
        if (str(answer6[i]) == 'Assez Satisfait'):
            q6_assez.append(answer6[i])
        if (str(answer7[i]) == 'Assez Satisfait'):
            q7_assez.append(answer7[i])
        if (str(answer8[i]) == 'Assez Satisfait'):
            q8_assez.append(answer8[i])
        if (str(answer9[i]) == 'Assez Satisfait'):
            q9_assez.append(answer9[i])
        if (str(answer11[i]) == 'Assez Satisfait'):
            q11_assez.append(answer11[i])
        if (str(answer12[i]) == 'Assez Satisfait'):
            q12_assez.append(answer12[i])
        if (str(answer13[i]) == 'Assez Satisfait'):
            q13_assez.append(answer13[i])
        if (str(answer13[i]) == 'Assez Satisfait'):
            q13_assez.append(answer13[i])
        if (str(answer14[i]) == 'Assez Satisfait'):
            q14_assez.append(answer14[i])
        if (str(answer15[i]) == 'Assez Satisfait'):
            q15_assez.append(answer15[i])

        ''' Très Satisfait'''
        if (str(answer2[i]) == 'Très Satisfait'):
            q2_tres.append(answer2[i])
        if (str(answer3[i]) == 'Très Satisfait'):
            q3_tres.append(answer3[i])
        if (str(answer4[i]) == 'Très Satisfait'):
            q4_tres.append(answer4[i])
        if (str(answer6[i]) == 'Très Satisfait'):
            q6_tres.append(answer6[i])
        if (str(answer7[i]) == 'Très Satisfait'):
            q7_tres.append(answer7[i])
        if (str(answer8[i]) == 'Très Satisfait'):
            q8_tres.append(answer8[i])
        if (str(answer9[i]) == 'Très Satisfait'):
            q9_tres.append(answer9[i])
        if (str(answer11[i]) == 'Très Satisfait'):
            q11_tres.append(answer11[i])
        if (str(answer12[i]) == 'Très Satisfait'):
            q12_tres.append(answer12[i])
        if (str(answer13[i]) == 'Très Satisfait'):
            q13_tres.append(answer13[i])
        if (str(answer13[i]) == 'Très Satisfait'):
            q13_tres.append(answer13[i])
        if (str(answer14[i]) == 'Très Satisfait'):
            q14_tres.append(answer14[i])
        if (str(answer15[i]) == 'Très Satisfait'):
            q15_tres.append(answer15[i])

    context = {'answer' : answer,
               'etudiant_count': etudiant_count,
               'q2_pas' : q2_pas, 'q3_pas' : q3_pas, 'q4_pas' : q4_pas, 'q6_pas' : q6_pas, 'q7_pas' : q7_pas, 'q8_pas' : q8_pas, 'q9_pas' : q9_pas, 'q11_pas' : q11_pas, 'q12_pas' : q12_pas, 'q13_pas' : q13_pas, 'q14_pas' : q14_pas, 'q15_pas' : q15_pas,
               'q2_peu' : q2_peu, 'q3_peu' : q3_peu, 'q4_peu' : q4_peu, 'q6_peu' : q6_peu, 'q7_peu' : q7_peu, 'q8_peu' : q8_peu, 'q9_peu' : q9_peu, 'q11_peu' : q11_peu, 'q12_peu' : q12_peu, 'q13_peu' : q13_peu, 'q14_peu' : q14_peu, 'q15_peu' : q15_peu,
               'q2_assez' : q2_assez, 'q3_assez' : q3_assez, 'q4_assez' : q4_assez, 'q6_assez' : q6_assez, 'q7_assez' : q7_assez, 'q8_assez' : q8_assez, 'q9_assez' : q9_assez, 'q11_assez' : q11_assez, 'q12_assez' : q12_assez, 'q13_assez' : q13_assez, 'q14_assez' : q14_assez, 'q15_assez' : q15_assez,
               'q2_tres': q2_tres, 'q3_tres' : q3_tres, 'q4_tres' : q4_tres, 'q6_tres' : q6_tres, 'q7_tres' : q7_tres, 'q8_tres' : q8_tres, 'q9_tres' : q9_tres, 'q11_tres' : q11_tres, 'q12_tres' : q12_tres, 'q13_tres' : q13_tres, 'q14_tres' : q14_tres, 'q15_tres' : q15_tres,
               'question': question,
               'professeur': professeur,}

    return render(request, "dashboard/dashboard_result.html", context)

def result_comment(request, grade_code, idx):
    question = Question.objects.all()
    professeur = Professeur.objects.all().filter(idx=idx)
    etudiant_count = Etudiant.objects.all().filter(professeur_idx_id=idx).count()

    ''' Answer de Contents '''
    answer1 = Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=1)
    answer5 = Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=5)
    answer10 = Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=10)
    answer16 = Answer.objects.all().filter(professeur_idx_id=idx).filter(question_idx_id=16)


    context = {'question': question,
               'professeur': professeur,
               'answer1': answer1,
               'answer5': answer5,
               'answer10': answer10,
               'answer16': answer16,
               'etudiant_count': etudiant_count,}
    return render(request, "dashboard/dashboard_result_comment.html", context)

from django.shortcuts import render, get_object_or_404
from epsi.models import Grade, Professeur, Etudiant, Answer, Question

def index(request):
    print("Hello")

    grade = Grade.objects.all
    
    context= {'grade' : grade}
    return render(request,'dashboard/dashboard_index.html', context)

def detail(request, grade_code):

    professeur = Professeur.objects.all().filter(grade_code=grade_code)
    print("context : professeur")
    print(professeur)
    context = {'professeur': professeur}

    return render(request, "dashboard/dashboard_grade.html", context)

def result(request, grade_code, idx):

    professeur = get_object_or_404(Professeur, pk=idx)
    etudiant = Etudiant.objects.all().filter(professeur_idx_id=professeur.idx)

    etudiant_count = Etudiant.objects.all().filter(professeur_idx_id=professeur.idx).count()
    print("etudiant_count")
    print(etudiant_count)

    etudiant_queryset_list = []
    for e in etudiant:
        etudiant_queryset_list.append(e)

    print("etudiant_queryset_list")
    print(etudiant_queryset_list)

    etudiant_idx_list =[]
    for i in range(etudiant_count):
        etudiant_idx_list.append(etudiant_queryset_list[i].idx)

    print("etudiant_idx_list")
    print(etudiant_idx_list)

    question_count = Question.objects.all().count()
    print(question_count)


    answer_list=[]
    for i in range(etudiant_count):
        answer_list.append(Answer.objects.filter(etudiant_idx_id=etudiant_idx_list[i]))


    print("answer_list - 1ere question")
    for i in range(etudiant_count):
        print(answer_list[i][0])

    print("answer_list - 2eme question")
    q2_pas=[]
    q2_peu=[]
    q2_assez=[]
    q2_tres=[]
    for i in range(etudiant_count):
        if str(answer_list[i][1]) == 'Pas Satisfait':
            print(answer_list[i][1])
            q2_pas.append(answer_list[i][1])
        elif str(answer_list[i][1]) == 'Peu Satisfait':
            print(answer_list[i][1])
            q2_peu.append(answer_list[i][1])
        elif str(answer_list[i][1]) == 'Assez Satisfait':
            print(answer_list[i][1])
            q2_assez.append(answer_list[i][1])
        elif str(answer_list[i][1]) == 'Très Satisfait':
            print(answer_list[i][1])
            q2_tres.append(answer_list[i][1])

    context = {'answer_list': answer_list,
               'q2_pas' : q2_pas,
               'q2_peu' : q2_peu,
               'q2_assez' : q2_assez,
               'q2_tres': q2_tres,}

    return render(request, "dashboard/dashboard_result.html", context)


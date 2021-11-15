from django.shortcuts import render, get_object_or_404
from epsi.models import Grade, Professeur, Etudiant, Answer, Question

def index(request):
    print("Hello")

    grade = Grade.objects.all

    context= {'grade' : grade}
    return render(request,'dashboard/dashboard_index.html', context)

def detail(request, grade_code):

    professeur = Professeur.objects.all().filter(grade_code=grade_code)
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




    '''
    print(etudiant.query)
    print(etudiant.values("idx"))
    '''


    return render(request, "dashboard/dashboard_result.html")


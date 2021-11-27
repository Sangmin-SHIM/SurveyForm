from django.contrib import admin
from .models import Professeur, Etudiant, Answer, Question, Grade

# Register your models here.
class ProfesseurAdmin(admin.ModelAdmin):

    list_display = ("professeur",
                    "grade",
                    "cours_donne")

    for p in Professeur.objects.all():
        if p.grade == "B1":
            p.grade_code = 1
        elif p.grade == "B2":
            p.grade_code = 2
        elif p.grade == "B3":
            p.grade_code = 3
        elif p.grade == "I1":
            p.grade_code = 4
        else:
            p.grade_code = 5
        p.save()

    readonly_fields = ["grade_code"]


class EtudiantAdmin(admin.ModelAdmin):
    readonly_fields = ["professeur_idx"]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question_idx",
                    "response",
                    "etudiant_idx",
                    "professeur_idx",)
    readonly_fields = ["response","question_idx", "etudiant_idx","professeur_idx"]
    ordering = ('idx',)


class QuestionAdmin(admin.ModelAdmin):
    ordering = ('idx',)

class GradeAdmin(admin.ModelAdmin):
    readonly_fields = ["grade", "grade_code"]


admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Grade, GradeAdmin)




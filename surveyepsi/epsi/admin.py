from django.contrib import admin
from .models import Professeur, Etudiant, Answer, Question

# Register your models here.
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ("professeur",
                    "grade",
                    "cours_donne")

class EtudiantAdmin(admin.ModelAdmin):
    readonly_fields = ["professeur_idx"]

class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ["question_idx", "etudiant_idx"]

class QuestionAdmin(admin.ModelAdmin):
    ordering = ('idx',)

admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)


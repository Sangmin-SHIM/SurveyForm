from django.db import models


# Create your models here.
class Professeur(models.Model):

    idx = models.AutoField(primary_key=True)
    professeur = models.CharField(max_length=30)
    grade = models.CharField(max_length=10)
    grade_code = models.IntegerField(null=True)
    cours_donne = models.CharField(max_length=30)


    class Meta:
        verbose_name_plural = "Professeur"

    def __str__(self):
        return self.professeur

class Question(models.Model):
    idx = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Question"

    def __str__(self):
        return self.question

class Etudiant(models.Model):
    idx = models.AutoField(primary_key=True)
    professeur_idx = models.ForeignKey("Professeur",on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Etudiant"

    def __str__(self):
        return str(self.idx)

class Answer(models.Model):
    idx = models.AutoField(primary_key=True)
    response = models.CharField(max_length=120)
    question_idx = models.ForeignKey("Question", on_delete=models.CASCADE)
    etudiant_idx = models.ForeignKey("Etudiant", on_delete=models.CASCADE)
    professeur_idx = models.ForeignKey("Professeur", on_delete=models.CASCADE,default='0')

    class Meta:
        verbose_name_plural = "Answer"

    def __str__(self):
        return self.response

class Grade(models.Model):
    idx = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=10)
    grade_code = models.IntegerField(default='1')

    class Meta:
        verbose_name_plural = "Grade"

    def __str__(self):
        return self.grade
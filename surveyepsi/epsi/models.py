from django.db import models


# Professor's name, grade of which professor takes and his cours name
class Professeur(models.Model):

    coursChoices = (
        ('B1','B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('I1', 'I1'),
        ('I2', 'I2'),
    )

    idx = models.AutoField(primary_key=True,default='0')
    professeur = models.CharField(max_length=30)
    grade = models.CharField(max_length=10, choices=coursChoices)
    grade_code = models.IntegerField(null=True)
    cours_donne = models.CharField(max_length=30)

    # Capitalized
    def save(self, *args, **kwargs):
        self.professeur = self.professeur.upper()
        self.grade = self.grade.upper()
        self.cours_donne = self.cours_donne.upper()
        return super(Professeur, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Professeur"

    # In Admin Page (/admin), we can recognize the data along the name of professor
    def __str__(self):
        return self.professeur


# Question content
class Question(models.Model):
    idx = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Question"

    def __str__(self):
        return self.question


# Student is related to professor (Student has the professor id as ForeignKey)
class Etudiant(models.Model):
    idx = models.AutoField(primary_key=True)
    professeur_idx = models.ForeignKey("Professeur",on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Etudiant"

    def __str__(self):
        return str(self.idx)

# Answer will be generated when student submits his survey. It has student id and professor id as ForeignKey)
class Answer(models.Model):
    idx = models.AutoField(primary_key=True)
    response = models.CharField(max_length=120)
    question_idx = models.ForeignKey("Question", on_delete=models.CASCADE,default='0')
    etudiant_idx = models.ForeignKey("Etudiant", on_delete=models.CASCADE,default='0')
    professeur_idx = models.ForeignKey("Professeur", on_delete=models.CASCADE,default='0')

    class Meta:
        verbose_name_plural = "Answer"

    def __str__(self):
        return self.response

# Grade consists of B1, B2, B3, I1 and I2. It has each grade code to use for rendering page
class Grade(models.Model):
    idx = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=10)
    grade_code = models.IntegerField(default='1')

    class Meta:
        verbose_name_plural = "Grade"

    def __str__(self):
        return self.grade
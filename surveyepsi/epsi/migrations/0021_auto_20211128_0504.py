# Generated by Django 3.1.2 on 2021-11-28 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsi', '0020_answer_professeur_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='etudiant_idx',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='epsi.etudiant'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_idx',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='epsi.question'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='idx',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='grade',
            field=models.CharField(choices=[('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('I1', 'I1'), ('I2', 'I2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='idx',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.1.2 on 2021-11-18 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsi', '0019_auto_20211110_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='professeur_idx',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='epsi.professeur'),
        ),
    ]
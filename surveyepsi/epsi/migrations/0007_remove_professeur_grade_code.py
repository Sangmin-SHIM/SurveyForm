# Generated by Django 3.1.2 on 2021-11-10 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epsi', '0006_auto_20211110_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professeur',
            name='grade_code',
        ),
    ]

# Generated by Django 3.1.2 on 2021-11-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epsi', '0015_auto_20211110_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='grade',
            field=models.CharField(choices=[('1', 'B1'), ('B2', '2'), ('B3', '3'), ('I1', '4'), ('I2', '5')], max_length=10),
        ),
    ]

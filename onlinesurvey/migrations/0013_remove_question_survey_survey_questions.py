# Generated by Django 4.2.1 on 2023-06-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesurvey', '0012_remove_answer_choice_answer_answer_choice_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='survey',
        ),
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(related_name='surveys', to='onlinesurvey.question'),
        ),
    ]

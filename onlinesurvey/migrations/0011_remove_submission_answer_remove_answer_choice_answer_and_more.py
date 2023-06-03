# Generated by Django 4.2.1 on 2023-06-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesurvey', '0010_rename_numeric_answer_answer_integer_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='choice_answer',
            field=models.ManyToManyField(related_name='answers', to='onlinesurvey.choice'),
        ),
    ]
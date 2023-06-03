# Generated by Django 4.2.1 on 2023-06-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesurvey', '0008_remove_submission_date_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='choice_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinesurvey.choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='date_answer',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='email_answer',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='numeric_answer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='short_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='text_answer',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='time_answer',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='onlinesurvey.question'),
        ),
    ]

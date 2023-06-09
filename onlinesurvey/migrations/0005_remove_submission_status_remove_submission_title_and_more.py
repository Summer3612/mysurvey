# Generated by Django 4.2.1 on 2023-06-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesurvey', '0004_alter_survey_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='status',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='widget_type',
            field=models.CharField(choices=[('RS', 'RadioSelect'), ('CSM', 'CheckboxSelectMultiple'), ('SS', 'Select')], default='RS', max_length=3),
        ),
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='survey',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 2.2.10 on 2020-08-04 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200804_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multichoicequestionitem',
            name='choice_question',
        ),
        migrations.AlterModelOptions(
            name='choicequestion',
            options={'verbose_name': 'Вопрос с вариантами', 'verbose_name_plural': 'Вопросы вариантами'},
        ),
        migrations.AlterField(
            model_name='choiceanswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.ChoiceQuestion', verbose_name='Вопрос с вариантами'),
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='answer',
        ),
        migrations.AddField(
            model_name='multichoiceanswer',
            name='answer',
            field=models.ManyToManyField(to='quiz.ChoiceQuestionItem', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='multichoiceanswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.ChoiceQuestion', verbose_name='Вопрос с вариантами'),
        ),
        migrations.DeleteModel(
            name='MultiChoiceQuestion',
        ),
        migrations.DeleteModel(
            name='MultiChoiceQuestionItem',
        ),
    ]

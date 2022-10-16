# Generated by Django 4.1.1 on 2022-10-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0011_study_method_tag_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='student',
            field=models.ManyToManyField(blank=True, to='groups.student'),
        ),
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='groups.question'),
        ),
        migrations.AddField(
            model_name='tag',
            name='study_method',
            field=models.ManyToManyField(blank=True, null=True, to='groups.study_method'),
        ),
        migrations.AlterField(
            model_name='question',
            name='statement',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='tag',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, to='groups.student'),
        ),
    ]

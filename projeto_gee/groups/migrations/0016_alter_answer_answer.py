# Generated by Django 4.1.1 on 2022-11-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0015_alter_question_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=10),
        ),
    ]

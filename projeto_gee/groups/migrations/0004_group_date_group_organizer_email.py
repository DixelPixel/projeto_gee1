# Generated by Django 4.1.1 on 2022-09-28 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_student_group_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='date',
            field=models.DateField(default='2021-04-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='organizer_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0016_alter_answer_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='confirmar',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='nome',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='senha',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='usuario',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
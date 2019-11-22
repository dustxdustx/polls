# Generated by Django 2.2.7 on 2019-11-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191118_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='选项描述'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='票数'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='问题描述'),
        ),
    ]
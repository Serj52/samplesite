# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-19 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Haзвaниe')),
            ],
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Rubric', verbose_name='Рубрика'),
        ),
    ]
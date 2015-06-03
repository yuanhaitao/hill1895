# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('head_pic_url', models.CharField(max_length=250, null=True, verbose_name='\u5934\u56fe\u94fe\u63a5', blank=True)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='\u6b63\u6587')),
                ('page_views', models.PositiveIntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf', editable=False)),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_1', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_2', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category1',
            field=models.ForeignKey(to='hill1895.Category1'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category2',
            field=models.ForeignKey(to='hill1895.Category2', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='hill1895.Tag', blank=True),
        ),
    ]

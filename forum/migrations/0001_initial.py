# Generated by Django 2.1.7 on 2020-07-17 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('sort', models.IntegerField()),
                ('son_sort', models.IntegerField()),
                ('content', utils.models.RichTextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('is_top', models.BooleanField(default=False)),
                ('is_nice', models.BooleanField(default=False)),
                ('is_light', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'forumPost',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='ForumReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_id', models.IntegerField()),
                ('content', utils.models.RichTextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('floor', models.IntegerField()),
                ('is_top', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'forumReply',
                'ordering': ('-create_time',),
            },
        ),
    ]
